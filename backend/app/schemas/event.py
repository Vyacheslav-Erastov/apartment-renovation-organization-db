from datetime import datetime, time
from uuid import UUID
from pydantic import BaseModel


class EventBase(BaseModel):
    event_path: str
    video_title: str | None = None
    rtsp_link: str | None = None
    rtsp_time: datetime | None = None
    video_time: time | None = None

    class Config:
        orm_mode = True


class EventUpdate(EventBase):
    pass


class Event(EventBase):
    id: UUID
    task_id: UUID


class EventCreate(Event):
    pass
