# app/main.py

from fastapi import FastAPI, HTTPException, Query
from typing import Optional
from app.data import transactions, alerts, analytics

app = FastAPI(title="Financial Data API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Financial Data API"}

@app.get("/transactions")
def get_transactions(min_amount: Optional[float] = Query(None), max_amount: Optional[float] = Query(None)):
    filtered = transactions
    if min_amount is not None:
        filtered = [t for t in filtered if t["amount"] >= min_amount]
    if max_amount is not None:
        filtered = [t for t in filtered if t["amount"] <= max_amount]
    return filtered

@app.get("/alerts")
def get_alerts(alert_type: Optional[str] = Query(None)):
    if alert_type:
        filtered = [a for a in alerts if a["alert_type"].lower() == alert_type.lower()]
        return filtered
    return alerts

@app.get("/analytics")
def get_analytics():
    return analytics
