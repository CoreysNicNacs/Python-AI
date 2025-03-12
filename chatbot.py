import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()

def chatbot_response(user_input):
    user_input = user_input.lower()
    tokens = word_tokenize(user_input)
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    processed_input = " ".join(lemmatized_tokens)

    if processed_input in responses:
        return responses[processed_input]

    # Regular expressions
    if re.search(r"what is the (.*) weather\?", user_input):
        return "I cannot provide weather information."

    if re.search(r"tell me a joke", user_input):
        return "Why don't scientists trust atoms? Because they make up everything!"

    else:
        return responses["default"]




responses = {
    "hello": "Hi there!",
    "how are you ?": "I'm doing well, thank you!",
    "what is your name ?": "I'm a simple chatbot.",
    "bye": "Goodbye!",
    "default": "I don't understand. Please try again.",
    "what time is it ?": "I don't have access to the current time.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "what is the weather ?": "I cannot provide weather information."
}

print("Chatbot: Hi! I'm ready to chat. Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
