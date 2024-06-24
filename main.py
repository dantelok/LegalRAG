from src.llm import generate_response
from src.prompt import prompt_template

if __name__ == '__main__':
    while True:
        question = input("：你好，請問有咩幫到你？\n")
        answer, memory = generate_response(question, prompt_template)

        print(f"：{answer}\n")
        print(f"Memory: {memory}\n")
