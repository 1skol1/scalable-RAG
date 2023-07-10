import os
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from typing import List


from core.errors import PredictException, ModelLoadException
from core.config import MODEL_PATH,QDRANT_URL


class MachineLearningModelHandlerScore(object):

    def __init__(self, collection_name):
        self.collection_name = collection_name
        # Initialize encoder model
        self.model = SentenceTransformer(MODEL_PATH, device='cpu')
        # initialize Qdrant client
        self.qdrant_client = QdrantClient(QDRANT_URL)
        

    def gen_embedding(self, text: str):
        # Convert text query into vector
        vector = self.model.encode(text).tolist()

        return vector

    def search(self, embed: List):
        
        # Use `vector` for search for closest vectors in the collection
        search_result = self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=embed,
            query_filter=None,  # If you don't want any filters for now
            limit=1  # 5 the most closest results is enough
        )
        # `search_result` contains found vector ids with similarity scores along with the stored payload
        # In this function you are interested in payload only
        payloads = [hit.payload for hit in search_result]
        return payloads

    def generate_response(self, context : str, usr_query: str):

        prompt_template = f'Answer based on context:\n\n{context}\n\n{usr_query}'


        return prompt_template
