from datetime import datetime
from uuid import UUID
from fastapi import Form
from pydantic import BaseModel

from app.models import OrderStatus
from app.schemas.work import Work


class OrderBase(BaseModel):
    start_date: datetime | None = None
    finish_date: datetime | None = None
    price: float | None = None
    status: OrderStatus

    class Config:
        from_attributes = True


class OrderUpdate(OrderBase):
    pass


class Order(OrderBase):
    client_id: int


class OrderIn(OrderBase):
    pass


class OrderCreate(Order):
    pass


class OrderTemplate(Order):
    id: int


class OrderForm(Order):

    @classmethod
    def as_form(
        cls,
        start_date: str = Form(),
        finish_date: str = Form(),
        price: float = Form(),
        status: OrderStatus = OrderStatus.CREATED,
        client_id: int = Form(),
    ):
        return cls(
            start_date=start_date,
            finish_date=finish_date,
            price=price,
            status=status,
            client_id=client_id,
        )


class OrderDetailed(Order):
    works: list["Work"] = []
