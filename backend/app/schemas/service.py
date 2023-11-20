from uuid import UUID
from pydantic import BaseModel


class ServiceBase(BaseModel):
    name: str
    description: str
    price: float

    class Config:
        orm_mode = True


class ServiceUpdate(ServiceBase):
    pass


class Service(ServiceBase):
    id: int


class ServiceIn(Service):
    pass


class ServiceCreate(Service):
    pass
