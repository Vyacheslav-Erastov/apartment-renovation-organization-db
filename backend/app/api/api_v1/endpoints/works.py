from uuid import UUID, uuid4
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas
from app import crud
from app.api import dependencies as deps

router = APIRouter()


@router.get("/", response_model=list[schemas.Work])
def read_works(
    db: Session = Depends(deps.get_db),
):
    works = crud.work.get_multi(db=db)
    return works


@router.post("/", response_model=schemas.Work)
def create_work(
    work_in: schemas.WorkCreate,
    db: Session = Depends(deps.get_db),
):
    try:
        work_in.id = uuid4()
        work = crud.work.create(db=db, obj_in=work_in)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    return work


@router.post("/multi", response_model=list[schemas.Work])
def create_works(
    works_in: list[schemas.WorkCreate],
    db: Session = Depends(deps.get_db),
):
    for work_in in works_in:
        try:
            work_in.id = uuid4()
            work = crud.work.create(db=db, obj_in=work_in)
            db.commit()
        except Exception as e:
            db.rollback()
            print(e)
    return works_in


@router.put("/{work_id}", response_model=schemas.Work)
def update_work(
    work_id: UUID,
    work_in: schemas.WorkUpdate,
    db: Session = Depends(deps.get_db),
):
    try:
        work = crud.work.update(db=db, obj_in=work_in, _id=work_id)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    return work


@router.delete("/")
def delete_work(work_id: UUID, db: Session = Depends(deps.get_db)):
    crud.work.remove(db=db, _id=work_id)
    return work_id
