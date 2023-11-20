from uuid import UUID
from pydantic import BaseModel
from app.schemas.order import Order


class ClientBase(BaseModel):
    first_name: str
    second_name: str
    phone_number: str
    email: str | None = None
    address: str

    class Config:
        orm_mode = True


class ClientUpdate(ClientBase):
    pass


class Client(ClientBase):
    id: UUID


class ClientIn(Client):
    pass


class ClientCreate(Client):
    id: int | None = None


class ClientDetailed(Client):
    orders: list["Order"] = []
