from langchain.chains import RetrievalQA
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain, ConversationChain


# QA chain without memory
def retrieval_qa(llm, db, prompt):
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=db.as_retriever(),
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )
    return qa_chain


# Conversational chain
def conversational_qa(llm, prompt):
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    conversational_chain = ConversationChain.from_llm(
        llm,
        memory=memory,
        # return_source_documents=True,
        combine_docs_chain_kwargs={"prompt": prompt}
    )

    return conversational_chain, memory


# Conversational QA chain
def conversational_retrieval_qa(llm, db, prompt):
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    retriever = db.as_retriever()
    conversational_chain = ConversationalRetrievalChain.from_llm(
        llm,
        retriever=retriever,
        memory=memory,
        # return_source_documents=True,
        combine_docs_chain_kwargs={"prompt": prompt}
    )

    return conversational_chain, memory


# Use for RetrievalQA ONLY
def query_retrieval(qa_chain, query):
    result = qa_chain.invoke({"query": query})
    answer = result["result"]
    source = result["source_documents"]
    return answer, source


# Use for Conversational QA chain ONLY
def question_answering_conversation(conversational_chain, question):
    result = conversational_chain.invoke({"question": question})
    answer = result["answer"]
    return answer
