from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_community.vectorstores.utils import filter_complex_metadata
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma


def data_loader(files):
    loader = UnstructuredFileLoader(files, strategy="hi_res", mode="elements")
    # Load files content
    docs = loader.load()

    # Remove irrelevant metadata
    docs = filter_complex_metadata(docs)

    # Splitter for splitting text
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=10000, chunk_overlap=0
    )

    data = text_splitter.split_documents(docs)

    return data


# Load vector database from file
def load_vector_store(file_path, embeddings):
    db = Chroma(persist_directory=file_path, embedding_function=embeddings)
    # print(db.get())
    # print(db.get()['metadatas'][-10:])
    return db

