from uuid import UUID, uuid4
from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app import schemas
from app import crud
from app.api import dependencies as deps

router = APIRouter()


templates = Jinja2Templates(directory="templates")


@router.get("/")
def read_services(
    request: Request,
    db: Session = Depends(deps.get_db),
):
    db_services = crud.service.get_multi(db=db)
    services = []
    for db_service in db_services:
        service = schemas.ServiceTemplate.from_orm(db_service).model_dump()
        services.append(service)
    return templates.TemplateResponse(
        request=request, name="services.html", context={"services": services}
    )


@router.post("/", response_model=schemas.Service)
def create_service(
    service_in: schemas.ServiceCreate,
    db: Session = Depends(deps.get_db),
):
    try:
        service_in.id = uuid4()
        service = crud.service.create(db=db, obj_in=service_in)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    return service


@router.post("/multi", response_model=list[schemas.Service])
def create_services(
    services_in: list[schemas.ServiceCreate],
    db: Session = Depends(deps.get_db),
):
    for service_in in services_in:
        try:
            service_in.id = uuid4()
            service = crud.service.create(db=db, obj_in=service_in)
            db.commit()
        except Exception as e:
            db.rollback()
            print(e)
    return services_in


@router.put("/{service_id}", response_model=schemas.Service)
def update_service(
    service_id: UUID,
    service_in: schemas.ServiceUpdate,
    db: Session = Depends(deps.get_db),
):
    try:
        service = crud.service.update(db=db, obj_in=service_in, _id=service_id)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    return service


@router.delete("/")
def delete_service(service_id: UUID, db: Session = Depends(deps.get_db)):
    crud.service.remove(db=db, _id=service_id)
    return service_id
