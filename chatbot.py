import nltk
from nltk.chat.util import Chat, reflections
pairs = [
    ["hi|hello|hey", ["Hello!", "Hi there!"]],
    ["how are you?", ["I'm good, thank you.", "I'm just a bot, but I'm functioning well!"]],
    ["what's your name?", ["I'm a chatbot.", "I'm just a bot."]],
    ["bye|goodbye", ["Goodbye!", "See you later!"]],
]
chatbot = Chat(pairs, reflections)
print("Hello! I'm a simple chatbot. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    response = chatbot.respond(user_input)
    print("Bot:", response)
