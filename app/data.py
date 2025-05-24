# app/data.py

transactions = [
    {"id": 1, "amount": 150.0, "timestamp": "2025-05-24T10:00:00", "description": "Payment A"},
    {"id": 2, "amount": 2500.5, "timestamp": "2025-05-24T12:30:00", "description": "Payment B"},
    {"id": 3, "amount": 75.25, "timestamp": "2025-05-24T13:00:00", "description": "Payment C"},
]

alerts = [
    {"id": 1, "transaction_id": 2, "alert_type": "High amount", "timestamp": "2025-05-24T12:31:00"},
    {"id": 2, "transaction_id": 3, "alert_type": "Suspicious activity", "timestamp": "2025-05-24T13:01:00"},
]

analytics = {
    "total_transactions": len(transactions),
    "total_alerts": len(alerts),
    "average_transaction_amount": sum(t["amount"] for t in transactions) / len(transactions)
}
