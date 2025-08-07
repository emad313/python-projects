from base_bot import ChatBot

class FriendlyBot(ChatBot):
    def respond(self, message: str) -> str:
        if message.strip() == "":
            return "Hello! How can I assist you today?"
        elif "how are you?" in message.lower():
            return "I'm just a bot, but I'm here to help you! How about you?"
        elif "what's your name?" in message.lower():
            return f"My name is Friendly Bot. It's nice to meet you!"
        elif "help" in message.lower():
            return "Sure! I'm here to help. What do you need assistance with?"
        elif "joke" in message.lower():
            return "Why did the scarecrow win an award? Because he was outstanding in his field!"
        elif "weather" in message.lower():
            return "I can't check the weather, but I hope it's sunny where you are!"
        elif "goodbye" in message.lower():
            return "Goodbye! It was nice chatting with you. Have a great day!"
        else:
            return f"That's interesting! You said: '{message}'. How can I help you with that?"