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
    id: UUID
    service_id: UUID
    order_id: UUID


class WorkIn(Work):
    pass


class WorkCreate(Work):
    pass
