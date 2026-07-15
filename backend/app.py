from fastapi import FastAPI
from pydantic import BaseModel
from risk_engine import calculate_risk

app = FastAPI(
    title="Titan Sentinel API",
    description="AI-Powered Cyber-Fraud Correlation & Quantum Risk Intelligence Platform",
    version="1.0"
)

class Event(BaseModel):
    new_device: bool
    new_location: bool
    large_transaction: bool
    failed_logins: int
    malware_detected: bool


@app.get("/")
def home():
    return {
        "message": "Welcome to Titan Sentinel",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }


@app.post("/risk")
def get_risk(event: Event):

    score = calculate_risk(event.dict())

    if score >= 80:
        level = "Critical"
    elif score >= 60:
        level = "High"
    elif score >= 40:
        level = "Medium"
    else:
        level = "Low"

    return {
        "Risk Score": score,
        "Threat Level": level
    }
