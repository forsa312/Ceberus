from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from typing import Dict, Any, List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/dashboard")
def api_dashboard() -> Dict[str, Any]:


    return {
        "threat_level": "LOW",
        "anomalies_24h": 0,
        "devices": 1,
        "events_24h": 0,
    }

@app.get("/api/anomalies")
def api_anomalies() -> List[Dict[str, Any]]:
    return []

def main():
    uvicorn.run(app, host="127.0.0.1", port=5001)

if __name__ == "__main__":
    main()
