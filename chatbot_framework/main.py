from friendly_bot import FriendlyBot
from sarcastic_bot import SarcasticBot
from chat_session import start_chatbot


def choose_bot():
    print("Choose a chatbot: ")
    print("1. Friendly Bot")
    print("2. Sarcastic Bot")
    choice = input("Enter the number of your choice: ").strip()

    if choice == '1':
        return FriendlyBot(name="Friendly Bot")
    elif choice == '2':
        return SarcasticBot(name="Sarcastic Bot")
    else:
        print("Invalid choice. Defaulting to Friendly Bot.")
        return FriendlyBot(name="Friendly Bot")
    
def main():
    bot = choose_bot()
    start_chatbot(bot)

if __name__ == "__main__":
    main()