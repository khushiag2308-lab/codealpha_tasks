
print("================================")
print("SIMPLE CHATBOT")
print("================================")
print("Type 'bye' to exit the chatbot.")

while True:

    user = input("\nYou: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How can I help you?")

    elif "how are you" in user:
        print("Bot: I am fine. Thank you for asking!")

    elif "your name" in user:
        print("Bot: My name is Python Chatbot.")

    elif "who are you" in user:
        print("Bot: I am a simple chatbot created using Python.")

    elif "what can you do" in user:
        print("Bot: I can answer some basic questions and have a simple conversation.")

    elif "thank you" in user or "thanks" in user:
        print("Bot: You're welcome!")

    elif "good morning" in user:
        print("Bot: Good morning! Have a great day.")

    elif "good night" in user:
        print("Bot: Good night! Sleep well.")

    elif user == "bye" or user == "exit":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")