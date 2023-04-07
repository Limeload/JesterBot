import random

# Define global variables to store the chat history and the user's name
chat_history = []
user_name = ""

# Define your main function
def main():
    # Print a welcome message and ask for the user's name
    global user_name
    print("Welcome to my chatbot!")
    user_name = input("What's your name? ")

    # Start a loop to keep the chatbot running
    while True:
        # Get user input
        user_input = input(f"{user_name}: ")

        # Add the user's input to the chat history
        chat_history.append(user_input)

        # Generate a response based on the chat history
        bot_response = generate_response(chat_history)

        # Add the bot's response to the chat history
        chat_history.append(bot_response)

        # Print the bot's response
        print(f"Bot: {bot_response}")

        # Check if the user wants to quit
        if user_input.lower() == "quit":
            print("Thank you for chatting! Goodbye.")
            break

# Define a function to generate the bot's response
def generate_response(chat_history):
    # Define a list of possible responses
    responses = ["I'm not sure what you mean.",
                 "Can you please rephrase that?",
                 "Interesting, tell me more.",
                 "Why do you say that?",
                 "That's a good point.",
                 "I'm sorry, I don't understand.",
                 "Let's talk about something else."]

    # Check if this is the first interaction with the user
    if len(chat_history) == 1:
        return f"Nice to meet you, {user_name}! How can I help you today?"

    # Check if the user has asked a question in the previous message
    if "?" in chat_history[-2]:
        return "I'm not sure, what do you think?"

    # Check if the user has mentioned a topic in the previous message
    keywords = ["weather", "sports", "movies", "music", "food"]
    for word in chat_history[-2].split():
        if word.lower() in keywords:
            return f"I also like {word.lower()}! What's your favorite {word.lower()}?"

    # If none of the above conditions are met, return a random response
    return random.choice(responses)

# Call the main function
if __name__ == "__main__":
    main()
