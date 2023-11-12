import os
import time
from uuid import uuid4
from app.api.dependencies import get_db
from app import crud
from app import schemas
from app.core.config import settings
from app.models.task import TaskStatus


class BaseDetector:
    def __init__(self, task_id, task_type, rtsp_links: list[str] | None = None) -> None:
        self._task_id = task_id
        self._task_type = task_type
        self._rtsp_links = rtsp_links
        self._db = next(get_db())

    def perform_detection(self):
        try:
            print("ok")
            time.sleep(10)
            event = crud.event.create(
                db=self._db,
                obj_in=schemas.EventCreate(
                    id=uuid4(),
                    task_id=self._task_id,
                    event_path="test.jpg",
                    video_title="test.mp4",
                ),
            )
            task = crud.task.update(
                db=self._db,
                obj_in=schemas.TaskUpdate(status=TaskStatus.COMPLETED),
                _id=self._task_id,
            )
        except Exception as e:
            print(e)
            task = crud.task.update(
                db=self._db,
                obj_in=schemas.TaskUpdate(status=TaskStatus.ERROR),
                _id=self._task_id,
            )
