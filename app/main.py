from fastapi import FastAPI
import os
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"ok": True}

if __name__ == "__main__":
    # Use PORT env variable injected by Cloud Run / GKE
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
