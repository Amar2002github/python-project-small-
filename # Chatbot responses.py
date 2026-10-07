# Chatbot responses
import random
from datetime import datetime

# Chatbot responses
responses = {
    "hello": [
        "Hello! 👋",
        "Hi! How can I help you?",
        "Hey! Nice to meet you!"
    ],
    "how are you": [
        "I'm doing great! 😊",
        "I'm fine, thanks for asking!",
        "I'm ready to help you!"
    ],
    "name": [
        "My name is PyBot ",
        "You can call me PyBot."
    ],
    "python": [
        "Python is a popular programming language.",
        "Python is widely used for AI, web development, automation and data science."
    ],
    "bye": [
        "Goodbye! 👋",
        "See you later!",
        "Have a great day!"
    ]
}


def chatbot(message):
    message = message.lower().strip()

    if "hello" in message or "hi" in message or "hey" in message:
        return random.choice(responses["hello"])

    elif "how are you" in message:
        return random.choice(responses["how are you"])

    elif "your name" in message or "who are you" in message:
        return random.choice(responses["name"])

    elif "python" in message:
        return random.choice(responses["python"])

    elif "time" in message:
        return "The current time is " + datetime.now().strftime("%I:%M:%S %p")

    elif "bye" in message or "exit" in message or "quit" in message:
        return random.choice(responses["bye"])

    else:
        return "Sorry, I don't understand that yet. 🤔"


print("=" * 45)
print("         PYTHON AI CHATBOT")
print("=" * 45)
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower().strip() in ["bye", "exit", "quit"]:
        print("Bot:", random.choice(responses["bye"]))
        break

    reply = chatbot(user_input)
    print("Bot:", reply)
