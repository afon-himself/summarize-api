from fastapi import FastAPI, Body, HTTPException
from model import model_pipeline
from pydantic import BaseModel, Field

app = FastAPI()

class SummarizeRequest(BaseModel):
    text: str = Field(..., max_length=2500)
    config: dict

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}

@app.post("/summarize")
def summarize(request: SummarizeRequest = Body(...)):
    if len(request.text) > 2500:
        raise HTTPException(status_code=400, detail="Text exceeds 2500 characters")
    summary = model_pipeline(request.text, request.config)
    return {"summary": summary}

