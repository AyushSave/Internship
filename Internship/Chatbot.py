# Task 8: Simple Rule-Based Chatbot

print("===================================")
print("       SIMPLE CHATBOT")
print("===================================")
print("Bot: Hello! I am your chatbot.")
print("Bot: You can ask me simple questions.")
print("Bot: Type 'bye' to end the conversation.")

while True:
    user_input = input("\nYou: ").strip().lower()

    if user_input in ["hello", "hi", "hey", "good morning", "good evening"]:
        print("Bot: Hello! Nice to meet you.")

    elif user_input == "how are you":
        print("Bot: I am fine, thank you! How are you?")

    elif user_input in ["what is your name", "what's your name", "your name"]:
        print("Bot: My name is SimpleBot.")

    elif user_input in ["who are you", "what are you"]:
        print("Bot: I am a simple rule-based chatbot created using Python.")

    elif user_input in ["what can you do", "help"]:
        print("Bot: I can respond to greetings and answer some basic questions.")

    elif user_input in ["thank you", "thanks", "thankyou"]:
        print("Bot: You're welcome!")

    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day!")
        break

    else:
        print("Bot: Sorry, I don't understand your question.")
