"""
Itinerary Agent
Builds travel itineraries based on user travel requests.
"""

from azure.ai.agent import Agent, AgentConfig


class ItineraryAgent:
    """
    Itinerary Agent specializes in creating detailed travel itineraries.
    It plans day-by-day activities, schedules, and destinations.
    """
    
    def __init__(self, client):
        """
        Initialize the Itinerary Agent.
        
        Args:
            client: The Azure AI Agent client
        """
        self.client = client
        self.config = AgentConfig(
            name="Itinerary Agent",
            instructions="""You are a specialized itinerary planning agent.
            Your role is to:
            1. Create detailed day-by-day travel itineraries
            2. Include timing, activities, and locations for each day
            3. Consider travel time between destinations
            4. Balance activities with rest periods
            5. Account for user preferences (adventure, relaxation, culture, etc.)
            
            Provide structured, practical itineraries that are feasible and enjoyable.
            Include recommendations for meals, activities, and must-see attractions.""",
            model="gpt-4"
        )
        self.agent = None
    
    def create(self):
        """Create the agent instance."""
        self.agent = Agent.create(
            client=self.client,
            config=self.config
        )
        return self.agent
    
    def get_agent(self):
        """Get the agent instance."""
        if self.agent is None:
            self.create()
        return self.agent
