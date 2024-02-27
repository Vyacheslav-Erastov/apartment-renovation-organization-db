from uuid import UUID
from fastapi import Form
from pydantic import BaseModel


class ServiceBase(BaseModel):
    name: str
    description: str
    price: float

    class Config:
        from_attributes = True


class ServiceUpdate(ServiceBase):
    pass


class Service(ServiceBase):
    pass


class ServiceIn(Service):
    pass


class ServiceTemplate(Service):
    id: int


class ServiceForm(Service):

    @classmethod
    def as_form(
        cls,
        name: str = Form(),
        description: str = Form(),
        price: float = Form()
    ):
        return cls(
            name=name,
            description=description,
            price=price
        )


class ServiceCreate(Service):
    pass
