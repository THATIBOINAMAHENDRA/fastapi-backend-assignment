from sqlalchemy import Column, String, DateTime
from datetime import datetime
from .database import Base

class PropertyRecord(Base):
    __tablename__ = "properties"

    id = Column(String, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    customer_mobile = Column(String, nullable=False)
    property_name = Column(String, nullable=False)
    property_type = Column(String)
    status = Column(String, default="NEW")
    created_at = Column(DateTime, default=datetime.utcnow)