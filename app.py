from fastapi import FastAPI
from pydantic import BaseModel

from src.chatbot import ChatBot
from src.dataloader import DataLoader


class UserInput(BaseModel):
    question: str


# Initialize FastAPI app
app = FastAPI()

# Initialize the DataLoader and ChatBot once at startup
data_loader = DataLoader()
chat_bot = ChatBot(vector_store_path='./VectorStore/')


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/chat")
def chat(user_input: UserInput):
    question = user_input.question
    answer, history = chat_bot.process_chat(question)

    return {"answer": answer, "history": history}


# Optional: Endpoint to load data
@app.post("/load_data")
def load_data(files: list[str]):
    data = data_loader.load_data(files)
    # Assuming you want to process and store the data in the vector store
    # You can extend the DataLoader or ChatBot classes with methods for handling this.
    return {"status": "Data loaded successfully", "num_docs": len(data)}
