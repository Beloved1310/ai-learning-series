"""
Basic Chatbot Starter Template
This is a simple chatbot that uses Gemini API to respond to user input.
"""

import os
from google.cloud import aiplatform
from vertexai.generative_models import GenerativeModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Vertex AI
PROJECT_ID = os.getenv("GCP_PROJECT_ID", "your-project-id")
LOCATION = os.getenv("GCP_LOCATION", "us-central1")

aiplatform.init(project=PROJECT_ID, location=LOCATION)


class SimpleBot:
    """A simple chatbot using Gemini API"""

    def __init__(self, system_prompt: str = None):
        """
        Initialize the chatbot.

        Args:
            system_prompt: Optional system prompt to set bot personality
        """
        self.model = GenerativeModel("gemini-1.5-flash")
        self.system_prompt = system_prompt or "You are a helpful assistant."
        self.conversation_history = []

    def chat(self, user_message: str) -> str:
        """
        Send a message and get a response.

        Args:
            user_message: The user's input message

        Returns:
            The bot's response
        """
        try:
            # Add user message to history
            self.conversation_history.append(
                {"role": "user", "content": user_message}
            )

            # Build the full prompt with system instruction and history
            messages = [
                {"role": "user", "content": self.system_prompt},
            ]

            # Add conversation history
            for msg in self.conversation_history:
                messages.append(msg)

            # Generate response
            response = self.model.generate_content(
                [msg["content"] for msg in messages]
            )

            # Extract response text
            bot_response = response.text

            # Add bot response to history
            self.conversation_history.append(
                {"role": "assistant", "content": bot_response}
            )

            return bot_response

        except Exception as e:
            error_msg = f"Error: {str(e)}"
            print(error_msg)
            return error_msg

    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []


def main():
    """Main function to run the chatbot"""
    print("🤖 Welcome to the Simple Chatbot!")
    print("Type 'quit' to exit, 'clear' to clear history\n")

    # Create bot with optional system prompt
    system_prompt = "You are a friendly and helpful AI assistant."
    bot = SimpleBot(system_prompt=system_prompt)

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            if user_input.lower() == "quit":
                print("Goodbye! 👋")
                break

            if user_input.lower() == "clear":
                bot.clear_history()
                print("Conversation history cleared.\n")
                continue

            # Get response from bot
            response = bot.chat(user_input)
            print(f"\nBot: {response}\n")

        except KeyboardInterrupt:
            print("\n\nGoodbye! 👋")
            break


if __name__ == "__main__":
    main()
