from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime

# SQLite DB file
DATABASE_URL = "sqlite:///./gesture_logs.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Table model
class GestureLog(Base):
    __tablename__ = "gesture_logs"
    id = Column(Integer, primary_key=True, index=True)
    gesture = Column(String, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    action = Column(String)

# Create tables
Base.metadata.create_all(bind=engine)

# Export session
db_session = SessionLocal()
