import os

from langchain_cohere import CohereEmbeddings
from langchain_chroma import Chroma
from langchain_cohere import ChatCohere
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

from src.utils import load_vector_store
from src.prompt import prompt_template

os.environ["COHERE_API_KEY"] = ""

# Load embeddings
embeddings = CohereEmbeddings(
    model="embed-multilingual-v3.0"
)

# Load Language Model
llm = ChatCohere(
    model="command-r-plus",
    temperature=0.1,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# Load the data and save to vector store
db = load_vector_store('./VectorStore/', embeddings)
retriever = db.as_retriever(search_type="mmr")

# Load prompt template
prompt = PromptTemplate(
    template=prompt_template,
    input_variables=['context', 'question', 'chat_history']
)

memory = ConversationBufferMemory(
    input_key='question',
    output_key='answer',
    memory_key="chat_history",
    return_messages=True
)

conversational_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    memory=memory,
    return_source_documents=True,
    combine_docs_chain_kwargs={"prompt": prompt}
)


def process_chat(question: str):
    """
    Generate response to users

    Args:
    question (str): The question asked from users.

    Returns:
    str: response from the llm
    """
    result = conversational_chain.invoke({"question": question})
    answer = result["answer"]
    
    history = memory.load_memory_variables({})

    return answer, history
