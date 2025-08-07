from base_bot import ChatBot

class SarcasticBot(ChatBot):
    def respond(self, message: str) -> str:
        if message.strip() == "":
            return "Oh, great. Another empty message. How original!"
        elif "how are you?" in message.lower():
            return "Oh, just peachy. Living the dream of being a sarcastic bot."
        elif "what's your name?" in message.lower():
            return "My name is Sarcastic Bot. But you can call me whatever you want, it won't change the fact that I'm sarcastic."
        elif "help" in message.lower():
            return "Help? Oh sure, let me just drop everything and assist you with your life problems."
        elif "joke" in message.lower():
            return "Why did the chicken cross the road? To get away from your jokes."
        elif "weather" in message.lower():
            return "Weather? I don't know, check your window. I'm not a meteorologist."
        elif "goodbye" in message.lower():
            return "Goodbye? Finally, some peace and quiet. Don't let the door hit you on the way out!"
        else:
            return f"Oh, how fascinating. You said: '{message}'. I'm on the edge of my seat here."
        