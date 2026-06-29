from beanie import Document
from datetime import datetime
from pydantic import Field
from typing import Optional, List
from decimal import Decimal
from app.models.order_item import OrderItem

class Order(Document):
    id: str = Field(alias="_id")
    user_id: Optional[str] = None
    total_amount: Decimal
    status: Optional[str] = None
    delivery_type: str
    delivery_address: Optional[str] = None
    special_instructions: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    items: List[OrderItem] = []

    @property
    def order_id(self) -> str:
        return self.id

    class Settings:
        name = "orders"
