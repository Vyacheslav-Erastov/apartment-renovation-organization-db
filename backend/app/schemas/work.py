from datetime import datetime
from uuid import UUID
from fastapi import Form
from pydantic import BaseModel


class WorkBase(BaseModel):
    start_date: datetime
    finish_date: datetime | None = None
    description: str | None = None

    class Config:
        from_attributes = True


class WorkUpdate(WorkBase):
    pass


class Work(WorkBase):
    service_id: int
    order_id: int
    employee_id: int


class WorkIn(Work):
    pass


class WorkTemplate(Work):
    id: int


class WorkForm(Work):

    @classmethod
    def as_form(
        cls,
        start_date: datetime = Form(),
        description: str = Form(),
        finish_date: datetime = Form(),
        service_id: int = Form(),
        order_id: int = Form(),
        employee_id: int = Form(),
    ):
        return cls(
            start_date=start_date, description=description, finish_date=finish_date
        )


class WorkCreate(Work):
    pass
