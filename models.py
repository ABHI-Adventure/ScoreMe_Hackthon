from sqlalchemy import Column, Integer, String, JSON
from database import Base

class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(String, unique=True)
    type = Column(String)
    status = Column(String)
    input_data = Column(JSON)

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(String)
    rule = Column(String)
    result = Column(String)
    reason = Column(String)