from base_bot import ChatBot

def start_chatbot(bot: ChatBot):
    chat_generator = bot.chat()
    next(chat_generator)  # Initialize the generator
    print(f"{bot.name} is ready to chat! Type 'exit' to end the chat.")
    while True:
        try:
            user_input = input("You: ")
            chat_generator.send(user_input)
        except StopIteration:
            break
