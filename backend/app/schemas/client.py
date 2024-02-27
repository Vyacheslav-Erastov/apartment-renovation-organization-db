from uuid import UUID
from fastapi import Form
from pydantic import BaseModel
from app.schemas.order import Order


class ClientBase(BaseModel):
    first_name: str
    second_name: str
    phone_number: str
    email: str | None = None
    address: str

    class Config:
        from_attributes = True


class ClientUpdate(ClientBase):
    pass


class Client(ClientBase):
    pass


class ClientIn(Client):
    pass


class ClientCreate(Client):
    pass


class ClientTemplate(Client):
    id: int


class ClientForm(Client):

    @classmethod
    def as_form(
        cls,
        first_name: str = Form(),
        second_name: str = Form(),
        phone_number: str = Form(),
        email: str | None = Form(),
        address: str = Form(),
    ):
        return cls(
            first_name=first_name,
            second_name=second_name,
            phone_number=phone_number,
            email=email,
            address=address,
        )


class ClientDetailed(Client):
    id: int
    orders: list["Order"] = []
