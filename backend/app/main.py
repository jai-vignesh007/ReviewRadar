from fastapi import FastAPI

app = FastAPI(
    title="ReviewRadar API",
    version="0.1.0",
    description="Turns customer reviews into themes, sentiment, and what to fix next.",
)


@app.get("/health")
def health():
    """Used by AWS to check the service is alive."""
    return {"status": "ok", "service": "reviewradar-api", "version": app.version}