from fastapi import FastAPI # pyright: ignore[reportMissingImports]
from orchestrator import run_pipeline

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Loan AI API Running"}

@app.post("/loan")
def process_loan(data: dict):
    result = run_pipeline(data)
    return result