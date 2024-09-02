from src.chatbot import ChatBot
from src.dataloader import DataLoader


def main():
    # Initialize the DataLoader and ChatBot
    data_loader = DataLoader()
    chat_bot = ChatBot(vector_store_path='./VectorStore/')

    # Example usage: process a chat
    answer, history = chat_bot.process_chat("這份文件的主要內容是什麼？")

    # Print the answer and chat history
    print("Answer:", answer)
    print("Chat History:", history)


if __name__ == "__main__":
    main()
