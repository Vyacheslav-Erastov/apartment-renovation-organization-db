import os
from uuid import UUID
from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app import schemas
from app import crud
from app.api import dependencies as deps
from app.core.config import settings

router = APIRouter()


@router.get("/", response_model=list[schemas.Event])
def read_events(
    db: Session = Depends(deps.get_db),
):
    events = crud.event.get_multi(db=db)
    return events


@router.get("/file", response_class=FileResponse)
def read_event_path(file_name: str, task_id: UUID):
    return os.path.join(settings.WORKING_DIRECTORY, "output", task_id, file_name)
