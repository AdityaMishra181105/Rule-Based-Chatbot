# Advanced Rule-Based Chatbot

print("===== Simple AI Chatbot =====")
print("Type 'bye' to stop chatting.\n")

while True:
    user = input("You: ").lower()

    responses = {
        "hello": "Hello! Nice to meet you.",
        "hi": "Hi there!",
        "how are you": "I am doing great!",
        "what is your name": "I am a Python Chatbot.",
        "who created you": "I was created using Python.",
        "help": "You can ask me basic questions.",
        "python": "Python is a programming language.",
        "ai": "Artificial Intelligence makes machines smart."
    }

    found = False

    for key in responses:
        if key in user:
            print("Bot:", responses[key])
            found = True
            break

    if user == "bye":
        print("Bot: Goodbye!")
        break

    if not found and user != "bye":
        print("Bot: Sorry, I don't understand.")