from src.llm import generate_response
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
    answer, memory = generate_response(question, prompt_template)

    return {"answer": answer, "memory": memory}

# if __name__ == '__main__':
#     while True:
#         question = input("：你好，請問有咩幫到你？\n")
#         answer, memory = generate_response(question, prompt_template)
# 
#         print(f"：{answer}\n")
#         print(f"Memory: {memory}\n")
