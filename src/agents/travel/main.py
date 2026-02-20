"""
Main entry point for the Multi-Agent Travel Planning System.
"""

import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.agent import AIAgentClient
from src.agents.travel import TravelGroupChat


def main():
    """
    Main function to run the travel planning multi-agent system.
    """
    # Load environment variables
    load_dotenv()
    
    # Get configuration from environment
    endpoint = os.getenv("AZURE_AI_FOUNDRY_ENDPOINT")
    
    if not endpoint:
        print("Error: AZURE_AI_FOUNDRY_ENDPOINT environment variable not set")
        print("Please set it in a .env file or as an environment variable")
        return
    
    # Initialize Azure AI client with credential
    credential = DefaultAzureCredential()
    client = AIAgentClient(
        endpoint=endpoint,
        credential=credential
    )
    
    # Create the travel group chat
    print("Initializing Multi-Agent Travel Planning System...")
    travel_system = TravelGroupChat(client)
    
    print("\n" + "="*60)
    print("Welcome to the AI Travel Planning Assistant!")
    print("="*60)
    print("\nOur team of specialized agents is ready to help you plan your trip:")
    print("  • Travel Agent - Your main point of contact")
    print("  • Itinerary Agent - Creates detailed day-by-day plans")
    print("  • Booking Agent - Researches costs and availability")
    print("  • Inspiration Agent - Suggests creative ideas")
    print("\nType 'exit' or 'quit' to end the conversation.\n")
    
    # Interactive conversation loop
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("\nThank you for using the AI Travel Planning Assistant!")
            print("Happy travels! 🌍✈️")
            break
        
        if not user_input:
            continue
        
        try:
            # Start conversation with the group chat
            result = travel_system.start_conversation(user_input)
            print(f"\n{result}\n")
            
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Please try again or type 'exit' to quit.\n")


if __name__ == "__main__":
    main()
