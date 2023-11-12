from datetime import datetime
import os
from typing import Annotated
from uuid import UUID, uuid4
from fastapi import File, Form, UploadFile
from pydantic import BaseModel

from app.models.task import TaskStatus, TaskType
from app.schemas.event import Event
from app.utils.utils import extract_files


class TaskBase(BaseModel):
    name: str
    type: TaskType
    status: TaskStatus
    video_titles: list[str] | None = None
    rtsp_links: list[str] | None = None
    start_time: datetime | None = None
    end_time: datetime | None = None

    class Config:
        orm_mode = True
        from_attributes = True


class TaskUpdate(TaskBase):
    name: str | None = None
    type: TaskType | None = None
    status: TaskStatus | None = None


class Task(TaskBase):
    id: UUID


class TaskIn(Task):
    id: UUID
    status: TaskStatus | None

    @classmethod
    def as_form(
        cls,
        name: str = Form(),
        type: TaskType = Form(),
        video_files: list[UploadFile] = File(default=None),
        rtsp_links: str | None = Form(default=None),
    ):
        id = uuid4()
        if video_files is not None:
            dest_dir = extract_files(file_objects=video_files, task_id=id)
            video_titles = os.listdir(dest_dir)
        return cls(
            id=id,
            name=name,
            type=type,
            status=TaskStatus.CREATED,
            video_titles=video_titles,
        )


class TaskCreate(Task):
    pass


class TaskDetailed(Task):
    events: list["Event"] = []
