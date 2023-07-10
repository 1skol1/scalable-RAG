from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

API_PREFIX = "/api"
VERSION = "0.1.0"
PROJECT_NAME: str = config("PROJECT_NAME", default="scalable-rag")
DEBUG: bool = config("DEBUG", cast=bool, default=True)

MODEL_PATH = config("MODEL_PATH", default="./bert-model/sentence-transformers_all-MiniLM-L6-v2")
QDRANT_SECRET_KEY: Secret = config("QDRANT_SECRET_KEY", cast=Secret, default="")
HF_SECRET_KEY: Secret = config("HF_SECRET_KEY", cast=Secret, default="")
QDRANT_URL = config("QDRANT_URL", default='http://localhost:6333')
HF_URL = config("HF_URL",default="")


