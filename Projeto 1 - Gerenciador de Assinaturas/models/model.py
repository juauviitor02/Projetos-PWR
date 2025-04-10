from sqlmodel import SQLModel, Field, create_engine, Relationship
from typing import Optional, ClassVar
from datetime import datetime
from decimal import Decimal

class Subscription(SQLModel, table=True):
    id: int = Field(primary_key=True)
    empresa: str
    site: Optional[str] = None
    data_assinatura: datetime
    valor: Decimal

class Payment(SQLModel, table=True):
    id: int = Field(primary_key=True)
    subscription_id: int = Field(foreign_key="subscription.id")
    empresa: str 
    date: datetime

