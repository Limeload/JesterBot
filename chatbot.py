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
def generate_response(user_input, context):
    # Define a list of possible responses
    if "tell me a joke" in user_input.lower():
        responses = ["Why did the tomato turn red? Because it saw the salad dressing!",
                     "Why did the scarecrow win an award? Because he was outstanding in his field!",
                     "Why don't scientists trust atoms? Because they make up everything!",
                     "Why don't skeletons fight each other? They don't have the guts!",
                     "What do you get when you cross a snowman and a shark? Frostbite!"]
    else:
        responses = ["I'm not sure what you mean.",
                     "Can you please rephrase that?",
                     "Interesting, tell me more.",
                     "Why do you say that?",
                     "That's a good point.",
                     "I'm sorry, I don't understand.",
                     "Let's talk about something else."]

    # Update context with current input
    context.append(user_input)

    # Use last two inputs for contextual response
    if len(context) > 1:
        previous_input = context[-2]
        if "hi" in previous_input.lower() or "hello" in previous_input.lower():
            responses.append("Hello again!")
        elif "how are you" in previous_input.lower():
            responses.append("I'm doing well, thank you. How about you?")

    # Return a randomly selected response
    return random.choice(responses)


# Call the main function
if __name__ == "__main__":
    main()
