from pydantic import BaseModel
from decimal import Decimal

class OrderItem(BaseModel):
    id: int
    item_id: str
    quantity: int
    price_at_purchase: Decimal
