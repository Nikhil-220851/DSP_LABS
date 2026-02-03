import json
import os
import datetime
import random
import time

FILE_NAME = "memory.json"

# -------------------------------------------------
# Intents with multiple responses (non-boring)
# -------------------------------------------------
intents = [
    {
        "keywords": ["hello", "hi", "hey"],
        "response": [
            "Hey there! 😊",
            "Hi! Nice to see you.",
            "Hello! What can I help you with?",
            "Hey! Ready to chat?"
        ]
    },
    {
        "keywords": ["your name", "who are you"],
        "response": [
            "I’m SmartBot — your friendly learning chatbot 😄",
            "People call me SmartBot.",
            "I’m a chatbot that can learn from you!"
        ]
    },
    {
        "keywords": ["prime minister"],
        "response": [
            "India’s Prime Minister is Narendra Modi.",
            "Narendra Modi is currently serving as the Prime Minister of India.",
            "The PM of India right now is Narendra Modi."
        ]
    },
    {
        "keywords": ["help"],
        "response": [
            "Ask me anything! If I don’t know it, you can teach me 😉",
            "I can answer questions and learn new things.",
            "I’m here to chat, learn, and remember."
        ]
    },
    {
        "keywords": ["time"],
        "response": lambda: f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"
    },
    {
        "keywords": ["date"],
        "response": lambda: f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}"
    }
]

# Exit keywords
exit_keywords = ["bye", "goodbye", "ok bye", "see you", "exit", "quit"]

# Learning prompts (to avoid boredom)
learning_prompts = [
    "Hmm 🤔 I don’t know that yet.",
    "That’s new to me!",
    "Interesting… I haven’t learned this yet.",
    "Oops 😅 I don’t have an answer for that."
]

teach_prompts = [
    "Want to teach me?",
    "Can you help me learn this?",
    "Shall I remember this for next time?"
]

success_prompts = [
    "Nice! I’ll remember that 😄",
    "Got it 👍 I’ve learned something new!",
    "Saved! Thanks for teaching me 🙌"
]

# -------------------------------------------------
# Utility functions
# -------------------------------------------------
def load_memory():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_memory(memory):
    with open(FILE_NAME, "w") as file:
        json.dump(memory, file, indent=4)

def typing_effect(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.01)
    print()

# -------------------------------------------------
# Intent matching
# -------------------------------------------------
def match_intent(user_input):
    for intent in intents:
        for keyword in intent["keywords"]:
            if keyword in user_input:

                response = intent["response"]

                if callable(response):
                    return response()

                if isinstance(response, list):
                    return random.choice(response)

                return response
    return None

# -------------------------------------------------
# Learned memory matching
# -------------------------------------------------
def match_memory(user_input, memory):
    for question, answer in memory.items():
        if question in user_input or user_input in question:
            return answer
    return None

# -------------------------------------------------
# Chatbot main loop
# -------------------------------------------------
def chatbot():
    print("🤖 SmartBot is online!")
    print("Type anything… say bye to exit.\n")

    memory = load_memory()

    while True:
        user_input = input("You: ").strip().lower()

        # Exit handling
        for word in exit_keywords:
            if word in user_input:
                typing_effect("🤖 SmartBot: Goodbye! Have a great day 👋")
                return

        # Predefined intents
        intent_response = match_intent(user_input)
        if intent_response:
            typing_effect("🤖 SmartBot: " + intent_response)
            continue

        # Learned responses
        memory_response = match_memory(user_input, memory)
        if memory_response:
            typing_effect("🤖 SmartBot: " + memory_response)
            continue

        # Learning mode
        typing_effect("🤖 SmartBot: " + random.choice(learning_prompts))
        teach = input("🤖 SmartBot: " + random.choice(teach_prompts) + " (yes/no): ").strip().lower()

        if teach == "yes":
            answer = input("🤖 SmartBot: What should I reply? ")
            memory[user_input] = answer
            save_memory(memory)
            typing_effect("🤖 SmartBot: " + random.choice(success_prompts))
        else:
            typing_effect("🤖 SmartBot: No worries! Let’s continue 😊")

# -------------------------------------------------
# Run chatbot
# -------------------------------------------------
chatbot()
