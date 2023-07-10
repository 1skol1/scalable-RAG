from pydantic import BaseModel


class MachineLearningResponse(BaseModel):
    response: str


class HealthResponse(BaseModel):
    status: bool


class MachineLearningDataInput(BaseModel):
    query: str

