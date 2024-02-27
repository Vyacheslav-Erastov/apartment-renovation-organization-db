from uuid import UUID
from fastapi import Form
from pydantic import BaseModel

from app.schemas.work import Work


class EmployeeBase(BaseModel):
    first_name: str
    second_name: str
    job_title: str
    phone_number: str
    email: str | None = None

    class Config:
        from_attributes = True


class EmployeeUpdate(EmployeeBase):
    pass


class Employee(EmployeeBase):
    pass


class EmployeeIn(Employee):
    pass


class EmployeeCreate(Employee):
    pass

class EmployeeTemplate(Employee):
    id: int

class EmployeeForm(Employee):

    @classmethod
    def as_form(
        cls,
        first_name: str = Form(),
        second_name: str = Form(),
        phone_number: str = Form(),
        email: str | None = Form(),
        job_title: str = Form(),
    ):
        return cls(
            first_name=first_name,
            second_name=second_name,
            phone_number=phone_number,
            email=email,
            job_title=job_title,
        )


class EmployeeDetailed(Employee):
    orders: list["Work"] = []
