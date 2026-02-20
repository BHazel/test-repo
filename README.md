# test-repo
A test repository: will probably be deleted in about 2 hours!

## Multi-Agent Travel Planning System

This repository contains a sophisticated multi-agent system built with the **Microsoft Agent Framework** targeting **Microsoft Foundry**. The system uses a **Group Chat workflow** to coordinate multiple specialized AI agents for comprehensive travel planning.

### Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your Azure AI Foundry endpoint
   ```

3. **Run the system:**
   ```bash
   python -m src.agents.travel.main
   ```

### System Architecture

The system consists of **4 specialized agents** working together:

- 🎯 **Travel Agent** (Orchestrator) - Main user interaction & coordination
- 📋 **Itinerary Agent** - Creates detailed day-by-day travel plans
- 💰 **Booking Agent** - Researches costs and availability
- ✨ **Inspiration Agent** - Suggests creative ideas and alternatives

### Documentation

For detailed documentation, see [src/agents/travel/README.md](src/agents/travel/README.md)

### Examples

Run the examples script to see the system in action:
```bash
python examples.py
```
