from datetime import datetime
from uuid import UUID
from pydantic import BaseModel

from app.models import OrderStatus
from app.schemas.work import Work


class OrderBase(BaseModel):
    start_date: datetime | None = None
    finish_date: datetime | None = None
    price: float | None = None
    status: OrderStatus

    class Config:
        orm_mode = True


class OrderUpdate(OrderBase):
    pass


class Order(OrderBase):
    id: UUID
    client_id: UUID


class OrderIn(OrderBase):
    pass


class OrderCreate(Order):
    pass


class OrderDetailed(Order):
    works: list["Work"] = []
