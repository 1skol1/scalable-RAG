# scalable-rag

This is a retrieval augemtned generator API that uses AWS Lambda, Qdrant VectorDB and LLM(FLan-T5-Xl) to provide scalable and efficient answer generation.

# Problem Statement 

To build a hosting architecture for a question answering AI model. The system should include using a vector database. Also the design of the system should be done assuming need to cater >1M requests daily.

# Approach

To create a system for serving AI model we need to understand the major differnce between web API and ML/DL API, that is that ML/DL APIs are compute intensive. And hence we create a architecture that is modularized as to make best use of compute resources. For storing the priori embeddings of our dataset we use a 
vectorDB, to understand the reasons for choosing vectorDB read this [link](https://www.pinecone.io/learn/series/faiss/). 

# Solution

We create the python API to serve the system in fastAPI. This fastAPI api is being deployed in AWS Lambda because of high availabilty & scaling capabilities of Lambda,For vectorDB we use Qdrant because of high RPS and low indexing time, for detailed comparison with other vectorDBs refer to this [link](https://qdrant.tech/benchmarks/). For hosting the LLM we use huggingface API however this is only for quick development, in production other approaches like dockerised model on K8s or on a single large GPU server should be tested. Components like ETL pipeline for Qdrant & prediction store, in the figure below, are not included in this repo but should be taken in consideration in production.

# Design Diagram

![alt text](https://github.com/1skol1/scalable-RAG/blob/master/rag.jpg?raw=true)


## Installation

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## For locally running Qdrant

```sh
docker pull qdrant/qdrant
```
And run

```sh
docker run -p 6333:6333 \
    -v $(pwd)/qdrant_storage:/qdrant/storage \
    qdrant/qdrant
```

## For Flan-T5-XXL

Sign up for huggingface & generate an API token. Follow the guide for deployment [here](https://huggingface.co/google/flan-t5-xxl)

