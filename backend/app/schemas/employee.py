from uuid import UUID
from pydantic import BaseModel

from app.schemas.work import Work


class EmployeeBase(BaseModel):
    first_name: str
    second_name: str
    job_title: str
    phone_number: str
    email: str | None = None

    class Config:
        orm_mode = True


class EmployeeUpdate(EmployeeBase):
    pass


class Employee(EmployeeBase):
    id: UUID


class EmployeeIn(Employee):
    pass


class EmployeeCreate(Employee):
    id: int | None = None


class EmployeeDetailed(Employee):
    orders: list["Work"] = []
