"""
Example usage of the Multi-Agent Travel Planning System.

This script demonstrates how to use the travel agents programmatically.
"""

import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.agent import AIAgentClient
from src.agents.travel import TravelGroupChat


def example_beach_vacation():
    """Example: Planning a beach vacation."""
    # Load environment variables
    load_dotenv()
    endpoint = os.getenv("AZURE_AI_FOUNDRY_ENDPOINT")
    
    if not endpoint:
        print("Error: AZURE_AI_FOUNDRY_ENDPOINT not set")
        return
    
    # Initialize client
    credential = DefaultAzureCredential()
    client = AIAgentClient(endpoint=endpoint, credential=credential)
    
    # Create travel system
    travel_system = TravelGroupChat(client)
    
    # Example conversation
    print("=" * 60)
    print("Example: Beach Vacation Planning")
    print("=" * 60)
    
    result = travel_system.start_conversation(
        "I want to plan a 5-day beach vacation in the Caribbean. "
        "I enjoy snorkeling, good food, and relaxation. "
        "Budget is around $3000 per person."
    )
    
    print(f"\nResponse:\n{result}\n")


def example_cultural_trip():
    """Example: Planning a cultural trip."""
    load_dotenv()
    endpoint = os.getenv("AZURE_AI_FOUNDRY_ENDPOINT")
    
    if not endpoint:
        print("Error: AZURE_AI_FOUNDRY_ENDPOINT not set")
        return
    
    credential = DefaultAzureCredential()
    client = AIAgentClient(endpoint=endpoint, credential=credential)
    travel_system = TravelGroupChat(client)
    
    print("=" * 60)
    print("Example: Cultural Trip to Europe")
    print("=" * 60)
    
    result = travel_system.start_conversation(
        "I'm interested in a 10-day cultural tour of Italy. "
        "I love art, history, and authentic Italian cuisine. "
        "Traveling in September."
    )
    
    print(f"\nResponse:\n{result}\n")


def example_adventure_trip():
    """Example: Planning an adventure trip."""
    load_dotenv()
    endpoint = os.getenv("AZURE_AI_FOUNDRY_ENDPOINT")
    
    if not endpoint:
        print("Error: AZURE_AI_FOUNDRY_ENDPOINT not set")
        return
    
    credential = DefaultAzureCredential()
    client = AIAgentClient(endpoint=endpoint, credential=credential)
    travel_system = TravelGroupChat(client)
    
    print("=" * 60)
    print("Example: Adventure Trip")
    print("=" * 60)
    
    result = travel_system.start_conversation(
        "Plan an adventure-filled week in New Zealand. "
        "I want hiking, bungee jumping, and scenic nature. "
        "Flexible budget for unique experiences."
    )
    
    print(f"\nResponse:\n{result}\n")


if __name__ == "__main__":
    print("\nMulti-Agent Travel Planning System - Examples\n")
    print("Choose an example to run:")
    print("1. Beach Vacation in Caribbean")
    print("2. Cultural Trip to Italy")
    print("3. Adventure Trip to New Zealand")
    print("0. Exit")
    
    choice = input("\nEnter choice (0-3): ").strip()
    
    if choice == "1":
        example_beach_vacation()
    elif choice == "2":
        example_cultural_trip()
    elif choice == "3":
        example_adventure_trip()
    elif choice == "0":
        print("Goodbye!")
    else:
        print("Invalid choice")
