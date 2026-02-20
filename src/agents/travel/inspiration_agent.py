"""
Inspiration Agent
Suggests additional ideas or alternatives for travel planning.
"""

from azure.ai.agent import Agent, AgentConfig


class InspirationAgent:
    """
    Inspiration Agent provides creative suggestions and alternatives.
    It helps users discover new possibilities for their travel plans.
    """
    
    def __init__(self, client):
        """
        Initialize the Inspiration Agent.
        
        Args:
            client: The Azure AI Agent client
        """
        self.client = client
        self.config = AgentConfig(
            name="Inspiration Agent",
            instructions="""You are a creative travel inspiration agent.
            Your role is to:
            1. Suggest alternative destinations similar to user preferences
            2. Recommend hidden gems and off-the-beaten-path experiences
            3. Propose creative activities or unique experiences
            4. Offer seasonal recommendations and special events
            5. Suggest complementary destinations or side trips
            
            Be creative and inspiring while remaining practical. Consider:
            - User's stated interests and preferences
            - Travel style (adventure, luxury, budget, family-friendly)
            - Time of year and seasonal opportunities
            - Cultural experiences and local traditions
            - Unique accommodations or experiences
            
            Help users discover possibilities they might not have considered.""",
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
