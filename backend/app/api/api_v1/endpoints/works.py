from uuid import UUID, uuid4
from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app import schemas
from app import crud
from app.api import dependencies as deps

router = APIRouter()


templates = Jinja2Templates(directory="templates")


@router.get("/")
def read_works(
    request: Request,
    db: Session = Depends(deps.get_db),
):
    db_works = crud.work.get_multi(db=db)
    works = []
    for db_work in db_works:
        work = schemas.WorkTemplate.from_orm(db_work).model_dump()
        works.append(work)
    return templates.TemplateResponse(
        request=request, name="works.html", context={"works": works}
    )


@router.post("/")
def create_work(
    request: Request,
    work_in: schemas.WorkCreate = Depends(schemas.WorkForm.as_form),
    db: Session = Depends(deps.get_db),
):
    try:
        work = crud.work.create(db=db, obj_in=work_in)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    return RedirectResponse(
        request.url_for("read_works"), status_code=status.HTTP_303_SEE_OTHER
    )


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
