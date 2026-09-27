from fastapi import FastAPI

app = FastAPI(
    title="AI Agent POC",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "application": "AI Agent POC",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }