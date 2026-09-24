from sqlalchemy import Column, Integer, String, Float, DateTime
import datetime
from database import Base

class Defect(Base):
    __tablename__ = "defects"

    id = Column(Integer, primary_key=True, index=True)
    image_name = Column(String, index=True)
    defect_type = Column(String)
    confidence = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)