from abc import ABC, abstractmethod

class ChatBot(ABC):
    """Abstract base class for a chatbot framework.

    This class defines the basic structure and methods that any chatbot should implement.
    """
    def __init__(self, name="ChatBot"):
        self.name = name

    @abstractmethod
    def respond(self, message: str) -> str:
        pass

    def chat(self):
        print(f"{self.name} is ready to chat!")
        print("Type 'exit' to end the chat.")

        while True:
            user_input = yield
            if user_input.lower() == 'exit':
                print(f"{self.name} has ended the chat.")
                break
            response = self.respond(user_input)
            print(f"{self.name}: {response}")
