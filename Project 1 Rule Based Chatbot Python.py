# Project : Rule Based Chatbot
# Tool : Python
# Benefit : Foundation for building smarter chatbots using machine learning and LLMs later

print("Chatbot: Hello! Type 'bye' to exit")

while True:
    user = input("You: ").lower()

    if user =="hello":
        print("Bot: Hi How are you?")
    elif user == "how are you":
        print("Bot: I am doing great.")
    elif user == "your name":
        print("Bot: I'm rule base chatbot.")
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand")    
    
