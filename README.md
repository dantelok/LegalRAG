# LegalRAG

## 1. WorkFlow
* Data Preprocessing done behind the scene, stored in VectorStore
* Load data from vector store in `src/utils.py`
* Create prompt template in `src/prompt.py`
* Call the OpenAI model, load all params into the chain in `src/chat.py`. Please paste your own LLM endpoint api key here.

## 2. Structure

├── data               
├── src     
│   ├── chat.py
│   ├── prompt.py           
│   └── utils.py        
├── VectorStore            
├── config.py  
├── main.py          
├── requirements.txt  
└── README.md

## 3. Notes
* Vector DB: Chroma DB
* Embedding model: `Cohere embed-multilingual-v3.0`
* LLM: `Cohere Command R+`

## 4. How to Run
* `pip install -r requirements.txt`
* Run `uvicorn main:app --host 0.0.0.0 --port 80`
* Get to `localhost:80/docs`
* Ask your question and wait for the answer