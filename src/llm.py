import os

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

from .qa_chain import retrieval_qa, conversational_retrieval_qa, question_answering_conversation, conversational_qa
from src.utils import load_vector_store

# Config
os.environ['OPENAI_API_KEY'] = '<api-key>'

def generate_response(question, prompt_template):
    """
    Generate response to users

    Args:
    question (str): The question asked from users.

    Returns:
    str: response from the llm
    """
    # Load OpenAI embeddings
    embeddings = OpenAIEmbeddings()

    # Load the data and save to vector store
    db = load_vector_store('./VectorStore/', embeddings)

    # Load prompt template
    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=['context', 'question']
    )

    # print(prompt)

    # Load LLM
    llm = ChatOpenAI(
        temperature=0,
        model_name='gpt-4'
    )

    # Build conversation chain with db
    conversational_chain, memory = conversational_retrieval_qa(llm, db, prompt)

    # For testing
    # sample_question = "我老公打我，有冇犯法？"

    # Question Answering
    answer = question_answering_conversation(conversational_chain, question)

    # print(f"Answer: {answer}")
    return answer, memory
