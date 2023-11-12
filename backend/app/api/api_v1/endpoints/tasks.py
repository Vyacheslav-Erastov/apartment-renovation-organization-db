from datetime import datetime
import threading
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas
from app import crud
from app.api import dependencies as deps
from app.modules.detectors.base_detector import BaseDetector

router = APIRouter()


@router.get("/", response_model=list[schemas.TaskDetailed])
def read_tasks(
    db: Session = Depends(deps.get_db),
):
    tasks = crud.task.get_multi(db=db)
    return tasks


@router.post("/", response_model=schemas.Task)
def create_task(
    task_in: schemas.TaskIn = Depends(schemas.TaskIn.as_form),
    db: Session = Depends(deps.get_db),
):
    try:
        task_create = schemas.TaskCreate(
            **task_in.dict(exclude_unset=True), start_time=datetime.now()
        )
        task = crud.task.create(db=db, obj_in=task_create)
        detector = BaseDetector(task_id=task_in.id, task_type=task_in.type)
        thread = threading.Thread(target=detector.perform_detection())
        thread.start()
    except Exception as e:
        print(e)
    return task_create


@router.delete("/")
def create_task(db: Session = Depends(deps.get_db)):
    tasks = crud.task.get_multi(db=db)
    for task in tasks:
        crud.task.remove(db=db, _id=schemas.Task.from_orm(task).id)
    return None
