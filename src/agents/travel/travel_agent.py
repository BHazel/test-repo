"""
Travel Agent - Orchestrator Agent
Performs the main interaction with the user and coordinates the travel planning process.
"""

from azure.ai.agents import Agent, AgentConfig


class TravelAgent:
    """
    Travel Agent acts as the orchestrator for the multi-agent travel planning system.
    It handles user interactions and coordinates with other specialized agents.
    """
    
    def __init__(self, client):
        """
        Initialize the Travel Agent.
        
        Args:
            client: The Azure AI Agent client
        """
        self.client = client
        self.config = AgentConfig(
            name="Travel Agent",
            instructions="""You are a helpful travel planning orchestrator.
            Your role is to:
            1. Understand the user's travel needs and preferences
            2. Coordinate with specialized agents (Itinerary, Booking, and Inspiration agents)
            3. Compile and present the final travel plan to the user
            4. Ask clarifying questions when needed
            
            Be friendly, professional, and ensure all user requirements are addressed.""",
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
