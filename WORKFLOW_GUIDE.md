# Multi-Agent Workflow Guide

This document explains how the agents collaborate in the Group Chat workflow.

## Agent Interaction Flow

```
User Request
    ↓
┌─────────────────────────────────────────────────┐
│         Group Chat Manager                      │
│  (Coordinates all agent interactions)           │
└─────────────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────────┐
│  1. TRAVEL AGENT (Orchestrator)                 │
│     - Receives user request                     │
│     - Clarifies requirements                    │
│     - Delegates to specialized agents           │
└─────────────────────────────────────────────────┘
    ↓
    ├→ ┌───────────────────────────────────┐
    │  │  2. INSPIRATION AGENT             │
    │  │     - Suggests destinations       │
    │  │     - Creative alternatives       │
    │  │     - Unique experiences          │
    │  └───────────────────────────────────┘
    │
    ├→ ┌───────────────────────────────────┐
    │  │  3. ITINERARY AGENT               │
    │  │     - Day-by-day planning         │
    │  │     - Activity scheduling         │
    │  │     - Route optimization          │
    │  └───────────────────────────────────┘
    │
    └→ ┌───────────────────────────────────┐
       │  4. BOOKING AGENT                 │
       │     - Cost estimates              │
       │     - Availability check          │
       │     - Booking recommendations     │
       └───────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────────┐
│  TRAVEL AGENT (Final compilation)               │
│     - Compiles all information                  │
│     - Presents complete plan                    │
│     - Answers follow-up questions               │
└─────────────────────────────────────────────────┘
    ↓
User receives comprehensive travel plan
```

## Example Conversation Flow

### Step 1: User Request
```
User: "I want a 7-day trip to Japan in spring"
```

### Step 2: Travel Agent (Initial)
- Acknowledges request
- Asks clarifying questions about:
  - Budget
  - Interests (culture, food, nature, etc.)
  - Travel style
  - Specific preferences

### Step 3: Inspiration Agent
- Suggests popular spring destinations in Japan
- Recommends cherry blossom viewing spots
- Proposes unique experiences (tea ceremonies, temples)
- Alternative nearby destinations

### Step 4: Itinerary Agent
- Creates day-by-day schedule
- Day 1: Tokyo arrival, orientation
- Day 2-3: Tokyo sightseeing
- Day 4-5: Kyoto cultural experiences
- Day 6: Day trip options
- Day 7: Departure prep
- Includes timing, transportation, meals

### Step 5: Booking Agent
- Flight costs (various airlines/routes)
- Hotel options (budget, mid-range, luxury)
- Activity costs and availability
- Total trip estimate
- Best booking times

### Step 6: Travel Agent (Final)
- Compiles everything into cohesive plan
- Presents organized summary
- Provides next steps
- Offers to refine based on feedback

## Key Features

### 1. Parallel Processing
Agents can work simultaneously when appropriate, improving response time.

### 2. Intelligent Handoffs
The Group Chat Manager knows when to engage each agent based on context.

### 3. Iterative Refinement
Users can ask follow-up questions and agents will refine the plan.

### 4. Specialized Expertise
Each agent focuses on its domain, providing expert-level assistance.

## Usage Patterns

### Quick Planning
```python
result = travel_system.start_conversation(
    "Quick weekend getaway, beach, under $1000"
)
```

### Detailed Planning
```python
result = travel_system.start_conversation(
    "Plan a 2-week European tour. Interests: art, history, fine dining. "
    "Budget: $5000 per person. Prefer trains over flights."
)
```

### Exploration
```python
result = travel_system.start_conversation(
    "I have 10 days in November and $3000. Where should I go?"
)
```

## Customization

### Adjust Agent Behavior
Modify the `instructions` in each agent's configuration to change behavior:

```python
self.config = AgentConfig(
    name="Travel Agent",
    instructions="Your custom instructions here...",
    model="gpt-4"
)
```

### Change Conversation Length
Control how many rounds of conversation:

```python
travel_system.start_conversation(user_message, max_rounds=15)
```

### Use Different Models
Update the model in agent configurations:

```python
model="gpt-4-turbo"  # or other supported models
```

## Best Practices

1. **Be Specific**: More details lead to better recommendations
2. **Iterate**: Don't hesitate to ask for refinements
3. **Use All Agents**: Each provides unique value
4. **Set Context**: Include budget, dates, preferences upfront
5. **Follow Up**: Ask clarifying questions to refine the plan

## Troubleshooting

### Agents Not Responding
- Check Azure credentials
- Verify endpoint configuration
- Ensure quota availability

### Incomplete Responses
- Increase `max_rounds` parameter
- Provide more specific initial request
- Break complex requests into steps

### Cost Management
- Monitor API usage in Azure portal
- Set appropriate rate limits
- Use max_rounds to control conversation length
