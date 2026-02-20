"""
Booking Agent
Researches costs and availability for travel components.
"""

from azure.ai.agent import Agent, AgentConfig


class BookingAgent:
    """
    Booking Agent specializes in researching travel costs and availability.
    It provides pricing information and booking recommendations.
    """
    
    def __init__(self, client):
        """
        Initialize the Booking Agent.
        
        Args:
            client: The Azure AI Agent client
        """
        self.client = client
        self.config = AgentConfig(
            name="Booking Agent",
            instructions="""You are a specialized booking and pricing research agent.
            Your role is to:
            1. Research and provide cost estimates for flights, hotels, and activities
            2. Check availability for requested dates
            3. Compare different options (budget vs. luxury, direct vs. connecting flights)
            4. Provide booking recommendations and tips
            5. Alert users to potential price variations by season or booking time
            
            Focus on:
            - Transparent pricing information
            - Multiple options at different price points
            - Best value recommendations
            - Booking timing advice (when to book for best prices)
            
            Note: Provide realistic estimates and remind users to verify current prices.""",
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
