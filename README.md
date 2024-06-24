# LegalRAG

## 1. WorkFlow
* Data Preprocessing done behind the scene, stored in VectorStore
* Load data from vector store in `src/utils.py`
* Create prompt template in `src/prompt.py`
* Build Conversational chain in `src/qa_chain.py`
* Call the OpenAI model, load all params into the chain in `src/llm.py`. Please paste your own OpenAI api key here.

## 2. Structure

├── data               
├── src     
│   ├── llm.py              
│   ├── utils.py     
│   ├── prompt.py           
│   └── qa_chain.py        
├── VectorStore            
├── config.py  
├── main.py          
├── requirements.txt  
└── README.md

## 3. Notes
* Vector DB: Chroma DB
* Embedding model: OpenAI
* LLM: GPT-4

## 4. How to Run
* `pip install -r requirements.txt`
* Run `python main.py`
* Ask your question and wait for the answer