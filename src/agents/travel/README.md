# Multi-Agent Travel Planning System

A sophisticated multi-agent system built with the Microsoft Agent Framework targeting Microsoft Foundry. The system uses a Group Chat workflow to coordinate multiple specialized AI agents for comprehensive travel planning.

## Architecture

The system consists of four specialized agents working together in a group chat configuration:

### 1. Travel Agent (Orchestrator)
- **Role**: Main point of contact with users
- **Responsibilities**:
  - Understand user travel needs and preferences
  - Coordinate with other specialized agents
  - Compile and present the final travel plan
  - Ask clarifying questions when needed

### 2. Itinerary Agent
- **Role**: Travel itinerary specialist
- **Responsibilities**:
  - Create detailed day-by-day travel itineraries
  - Plan timing, activities, and locations
  - Consider travel time between destinations
  - Balance activities with rest periods

### 3. Booking Agent
- **Role**: Cost and availability researcher
- **Responsibilities**:
  - Research cost estimates for flights, hotels, and activities
  - Check availability for requested dates
  - Compare different booking options
  - Provide booking recommendations and timing advice

### 4. Inspiration Agent
- **Role**: Creative travel ideation specialist
- **Responsibilities**:
  - Suggest alternative destinations
  - Recommend hidden gems and unique experiences
  - Propose creative activities
  - Offer seasonal recommendations

## Setup

### Prerequisites
- Python 3.8 or higher
- Azure subscription with access to Microsoft Foundry
- Azure AI Agent service configured

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd test-repo
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:

Create a `.env` file in the root directory with:
```
AZURE_AI_FOUNDRY_ENDPOINT=https://your-foundry-endpoint.azure.com
```

For authentication, ensure you have Azure credentials configured through one of:
- Azure CLI: `az login`
- Environment variables (AZURE_CLIENT_ID, AZURE_TENANT_ID, AZURE_CLIENT_SECRET)
- Managed Identity (when running in Azure)

## Usage

### Running the Interactive System

```bash
python -m src.agents.travel.main
```

This starts an interactive conversation where you can discuss your travel plans with the AI agents.

### Example Conversation

```
You: I want to plan a 7-day trip to Japan in spring

[The agents will collaborate to:]
- Understand your preferences and constraints
- Suggest creative destinations and experiences
- Create a detailed day-by-day itinerary
- Provide cost estimates and booking advice
```

### Programmatic Usage

You can also use the agents programmatically in your own code:

```python
from azure.identity import DefaultAzureCredential
from azure.ai.agent import AIAgentClient
from src.agents.travel import TravelGroupChat

# Initialize client
credential = DefaultAzureCredential()
client = AIAgentClient(
    endpoint="https://your-foundry-endpoint.azure.com",
    credential=credential
)

# Create travel system
travel_system = TravelGroupChat(client)

# Start conversation
result = travel_system.start_conversation(
    "I want to plan a beach vacation for my family"
)
```

## Project Structure

```
src/agents/travel/
├── __init__.py           # Package initialization
├── travel_agent.py       # Travel Agent (orchestrator)
├── itinerary_agent.py    # Itinerary Agent
├── booking_agent.py      # Booking Agent
├── inspiration_agent.py  # Inspiration Agent
├── group_chat.py         # Group Chat coordinator
├── main.py              # Main entry point
└── README.md            # This file
```

## Group Chat Workflow

The Group Chat workflow coordinates agent interactions:

1. **User Input**: Travel Agent receives the initial request
2. **Inspiration**: If needed, Inspiration Agent suggests creative ideas
3. **Planning**: Itinerary Agent creates the detailed schedule
4. **Costing**: Booking Agent provides pricing and availability
5. **Presentation**: Travel Agent compiles everything into a final plan

The Group Chat Manager ensures smooth handoffs between agents and that all user requirements are addressed.

## Features

- **Collaborative AI**: Multiple specialized agents work together
- **Comprehensive Planning**: Covers itinerary, costs, and inspiration
- **Interactive Conversation**: Natural dialogue with the AI team
- **Flexible Architecture**: Easy to extend with additional agents
- **Microsoft Foundry Integration**: Built for enterprise-grade AI deployment

## Configuration

### Agent Models
By default, all agents use GPT-4. You can modify the model in each agent's configuration:

```python
self.config = AgentConfig(
    name="Agent Name",
    instructions="...",
    model="gpt-4"  # Change to your preferred model
)
```

### Conversation Rounds
Control the maximum conversation rounds in group chat:

```python
travel_system.start_conversation(user_message, max_rounds=10)
```

## Troubleshooting

### Common Issues

1. **Authentication Errors**
   - Ensure Azure credentials are properly configured
   - Verify you have access to the Foundry endpoint
   - Check that the endpoint URL is correct

2. **Module Import Errors**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Verify you're running from the repository root directory

3. **Agent Creation Failures**
   - Check that your Azure AI Agent service is properly configured
   - Verify quota and rate limits in your Azure subscription

## Contributing

This is a test repository and may be deleted. For production use, please fork and maintain your own copy.

## License

This is a test repository. Check with the repository owner for licensing information.

## Support

For issues with:
- Microsoft Agent Framework: See [Azure AI documentation](https://learn.microsoft.com/azure/ai-services/)
- This implementation: Create an issue in the repository
