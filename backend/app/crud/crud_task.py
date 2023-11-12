from uuid import UUID
from sqlalchemy.orm import Session
from app.crud.crud_base import CRUDBase
from app.models.task import Task
from app import schemas
from app.schemas.task import TaskCreate, TaskUpdate
from app.core.connection_manager import manager


class CRUDTask(CRUDBase[Task, schemas.TaskCreate, schemas.TaskUpdate]):
    def create(self, db: Session, obj_in: TaskCreate) -> Task:
        result = super().create(db, obj_in)
        db.commit()
        manager.add_task(
            message=schemas.MessageWS(event=schemas.EventWS.TASK_CREATE, data=obj_in)
        )
        return result

    def update(self, db: Session, obj_in: TaskUpdate, _id: UUID) -> Task:
        result = super().update(db, obj_in, _id)
        db.commit()
        manager.add_task(
            message=schemas.MessageWS(event=schemas.EventWS.TASK_UPDATE, data=obj_in)
        )
        return result

    def remove(self, db: Session, _id: UUID) -> Task:
        result = super().remove(db, _id)
        db.commit()
        manager.add_task(
            message=schemas.MessageWS(event=schemas.EventWS.TASK_DELETE, data=_id)
        )
        return result


task = CRUDTask(Task)
