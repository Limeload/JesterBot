# Import necessary libraries
import random

# Define your main function
def main():
    # Print a welcome message
    print("Welcome to my chatbot!")

    # Start a loop to keep the chatbot running
    while True:
        # Get user input
        user_input = input("You: ")

        # Generate a response
        bot_response = generate_response(user_input)

        # Print the bot's response
        print("Bot: " + bot_response)

        # Check if the user wants to quit
        if user_input.lower() == "quit":
            print("Thank you for chatting! Goodbye.")
            break

# Define a function to generate the bot's response
def generate_response(user_input):
    # Define a list of possible responses
    responses = ["I'm not sure what you mean.",
                 "Can you please rephrase that?",
                 "Interesting, tell me more.",
                 "Why do you say that?",
                 "That's a good point.",
                 "I'm sorry, I don't understand.",
                 "Let's talk about something else."]

    # Return a randomly selected response
    return random.choice(responses)

# Call the main function
if __name__ == "__main__":
    main()
