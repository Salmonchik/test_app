import uuid

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import Column, String, func, DateTime, Float, ARRAY
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Figure(Base):
    __tablename__ = "figures"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    dimension = Column(Float, nullable=False)
    type = Column(String, nullable=False)
    color = Column(String, nullable=False)
    norm = ARRAY(Float)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
