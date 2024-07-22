from src.chat import process_chat
from src.prompt import prompt_template
from fastapi import FastAPI
from pydantic import BaseModel


class UserInput(BaseModel):
    question: str


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/chat")
def chat(question: str):
    answer, history = process_chat(question)

    return {"answer": answer, **history}


# if __name__ == '__main__':
#     while True:
#         question = input("：你好，請問有咩幫到你？\n")
#         answer, history = process_chat(question)
# 
#         print(f"：{answer}\n")
#         print(f"：{history}\n")
