"""
Group Chat Workflow
Coordinates multiple agents in a group chat configuration for travel planning.
"""

from azure.ai.agents import GroupChat, GroupChatManager
from .travel_agent import TravelAgent
from .itinerary_agent import ItineraryAgent
from .booking_agent import BookingAgent
from .inspiration_agent import InspirationAgent


class TravelGroupChat:
    """
    Manages a group chat workflow with multiple specialized travel agents.
    """
    
    def __init__(self, client):
        """
        Initialize the Travel Group Chat.
        
        Args:
            client: The Azure AI Agent client
        """
        self.client = client
        
        # Initialize all agents
        self.travel_agent = TravelAgent(client)
        self.itinerary_agent = ItineraryAgent(client)
        self.booking_agent = BookingAgent(client)
        self.inspiration_agent = InspirationAgent(client)
        
        self.agents = [
            self.travel_agent.get_agent(),
            self.itinerary_agent.get_agent(),
            self.booking_agent.get_agent(),
            self.inspiration_agent.get_agent()
        ]
        
        self.group_chat = None
        self.manager = None
    
    def create_group_chat(self, max_rounds=10):
        """
        Create the group chat with all agents.
        
        Args:
            max_rounds: Maximum number of conversation rounds
        
        Returns:
            The group chat manager
        """
        self.group_chat = GroupChat(
            agents=self.agents,
            messages=[],
            max_round=max_rounds
        )
        
        self.manager = GroupChatManager(
            groupchat=self.group_chat,
            instructions="""You are the group chat manager coordinating a team of travel planning agents.
            
            Agents in your team:
            - Travel Agent: The orchestrator who interacts with the user
            - Itinerary Agent: Creates detailed day-by-day itineraries
            - Booking Agent: Researches costs and availability
            - Inspiration Agent: Suggests creative ideas and alternatives
            
            Workflow:
            1. Start with the Travel Agent to understand user needs
            2. Bring in Inspiration Agent for creative suggestions if needed
            3. Have Itinerary Agent create the detailed plan
            4. Get Booking Agent to provide cost estimates and availability
            5. Let Travel Agent compile and present the final plan
            
            Ensure smooth handoffs between agents and that all user requirements are addressed.""",
            model="gpt-4"
        )
        
        return self.manager
    
    def start_conversation(self, user_message, max_rounds=10):
        """
        Start a conversation with the group chat.
        
        Args:
            user_message: Initial message from the user
            max_rounds: Maximum conversation rounds
        
        Returns:
            The conversation result
        """
        if self.manager is None:
            self.create_group_chat(max_rounds)
        
        # Start the conversation with the user message
        result = self.manager.initiate_chat(
            message=user_message,
            recipient=self.travel_agent.get_agent()
        )
        
        return result
