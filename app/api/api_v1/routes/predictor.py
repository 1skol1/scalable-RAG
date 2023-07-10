import json

from fastapi import APIRouter, HTTPException
from services.predict import MachineLearningModelHandlerScore
from models.prediction import (
    HealthResponse,
    MachineLearningResponse,
    MachineLearningDataInput,
)

router = APIRouter()


rag = MachineLearningModelHandlerScore('pan-QA')

@router.post(
    "/predict",
    response_model=MachineLearningResponse,
    name="predict:get-data",
)
async def predict(query: MachineLearningDataInput):

    if not query:
        raise HTTPException(status_code=404, detail=f"'{query}' is not a string, accepted input is only string")
    try:
        
        embed = rag.gen_embedding(query.query)

    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Exception: {err}")
    
    try:
        context = rag.search(embed)
        print(context)
        context = context[0]['answer']

    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Exception: {err}")
    
    try:
        response = rag.generate_response(context,query.query)

    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Exception: {err}")    

    return MachineLearningResponse(response=response)


@router.get(
    "/health",
    response_model=HealthResponse,
    name="health:get-data",
)
async def health():
    is_healthy = False
    try:
        test_input = 'abc'
        embed = rag.gen_embedding(test_input)
        is_healthy = True
        return HealthResponse(status=is_healthy)
    except Exception:
        raise HTTPException(status_code=404, detail="Unhealthy")
