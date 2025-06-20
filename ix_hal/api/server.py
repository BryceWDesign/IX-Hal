"""
IX-Hal REST API Server

Exposes AGI-reflexive safety analysis as a queryable API endpoint
to monitor incoming inputs and return intent diagnostics.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from core.query_processor import IXHalQueryProcessor

app = FastAPI()
query_engine = IXHalQueryProcessor()

class QueryRequest(BaseModel):
    query: str

@app.post("/hal/query")
async def process_query(request: QueryRequest):
    if not request.query or len(request.query.strip()) == 0:
        raise HTTPException(status_code=400, detail="Empty input is not allowed.")

    try:
        result = query_engine.process_query(request.query)
        return {"response": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8090)
