from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class WorkBase(BaseModel):
    start_date: datetime
    finish_date: datetime | None = None
    description: str | None = None

    class Config:
        orm_mode = True


class WorkUpdate(WorkBase):
    pass


class Work(WorkBase):
    id: int
    service_id: int
    order_id: int
    employee_id: int


class WorkIn(Work):
    pass


class WorkCreate(Work):
    pass
