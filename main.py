from fastapi import FastAPI, Body
from model import model_pipeline
from pydantic import BaseModel

app = FastAPI()

class SummarizeRequest(BaseModel):
    text: str
    config: dict

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}

@app.post("/summarize")
def summarize(request: SummarizeRequest = Body(...)):
    summary = model_pipeline(request.text, request.config)
    return {"summary": summary}

