# backend.py
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy import create_engine, Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# SQLite database setup
DATABASE_URL = "sqlite:///./trinetra_log.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
db_session = SessionLocal()

# DB Model
class GestureLog(Base):
    __tablename__ = "gesture_logs"
    id = Column(Integer, primary_key=True, index=True)
    gesture = Column(String)
    timestamp = Column(DateTime)
    action = Column(String)

# Create table
Base.metadata.create_all(bind=engine)

# API schema
class LogItem(BaseModel):
    gesture: str
    timestamp: datetime
    action: str

# API route
@app.post("/log")
def receive_log(item: LogItem):
    db_entry = GestureLog(
        gesture=item.gesture,
        timestamp=item.timestamp,
        action=item.action
    )
    db_session.add(db_entry)
    db_session.commit()
    print(f"[SAVED TO DB] {item}")
    return {"status": "logged to database"}
from fastapi.responses import JSONResponse

@app.get("/logs")
def get_all_logs():
    logs = db_session.query(GestureLog).all()
    return JSONResponse([
        {
            "id": log.id,
            "gesture": log.gesture,
            "timestamp": log.timestamp.isoformat(),
            "action": log.action
        }
        for log in logs
    ])
from fastapi import Query

@app.get("/logs/filter")
def get_logs_by_gesture(gesture: str = Query(..., description="Gesture to filter logs by")):
    filtered_logs = db_session.query(GestureLog).filter(GestureLog.gesture == gesture).all()
    return [
        {
            "id": log.id,
            "gesture": log.gesture,
            "timestamp": log.timestamp.isoformat(),
            "action": log.action
        }
        for log in filtered_logs
    ]
from fastapi import FastAPI, Query
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Session
from database import db_session, GestureLog  # Your DB setup and model

app = FastAPI()

class LogItem(BaseModel):
    gesture: str
    timestamp: datetime
    action: str

@app.post("/log")
def receive_log(item: LogItem):
    log = GestureLog(gesture=item.gesture, timestamp=item.timestamp, action=item.action)
    db_session.add(log)
    db_session.commit()
    return {"status": "ok"}

@app.get("/logs")
def get_all_logs():
    logs = db_session.query(GestureLog).order_by(GestureLog.timestamp.desc()).all()
    return [{
        "id": log.id,
        "gesture": log.gesture,
        "timestamp": log.timestamp.isoformat(),
        "action": log.action
    } for log in logs]

# 👇✅ PLACE THE NEW ROUTE HERE
@app.get("/logs/by-date")
def get_logs_by_date(
    start_date: Optional[datetime] = Query(None, description="Start date (ISO format)"),
    end_date: Optional[datetime] = Query(None, description="End date (ISO format)")
):
    query = db_session.query(GestureLog)

    if start_date:
        query = query.filter(GestureLog.timestamp >= start_date)
    if end_date:
        query = query.filter(GestureLog.timestamp <= end_date)

    logs = query.order_by(GestureLog.timestamp.desc()).all()

    return [
        {
            "id": log.id,
            "gesture": log.gesture,
            "timestamp": log.timestamp.isoformat(),
            "action": log.action
        }
        for log in logs
    ]
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
