from uuid import UUID, uuid4
from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app import schemas
from app import crud
from app.api import dependencies as deps

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/", response_model=list[schemas.ClientDetailed])
def read_clients(request: Request, db: Session = Depends(deps.get_db)):
    db_clients = crud.client.get_multi(db=db)
    clients = []
    for db_client in db_clients:
        client = schemas.ClientTemplate.from_orm(db_client).model_dump()
        clients.append(client)
    return templates.TemplateResponse(
        request=request, name="clients.html", context={"clients": clients}
    )


@router.post("/", response_model=schemas.Client)
def create_client(
    client_in: schemas.ClientCreate = Depends(schemas.ClientForm.as_form),
    db: Session = Depends(deps.get_db),
):
    try:
        client = crud.client.create(db=db, obj_in=client_in)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    return client


@router.post("/multi", response_model=list[schemas.Client])
def create_clients(
    clients_in: list[schemas.ClientCreate],
    db: Session = Depends(deps.get_db),
):
    for client_in in clients_in:
        try:
            client = crud.client.create(db=db, obj_in=client_in)
            db.commit()
        except Exception as e:
            db.rollback()
            print(e)
    return clients_in


@router.put("/{client_id}", response_model=schemas.Client)
def update_client(
    client_id: int,
    client_in: schemas.ClientUpdate,
    db: Session = Depends(deps.get_db),
):
    try:
        client = crud.client.update(db=db, obj_in=client_in, _id=client_id)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    return client


@router.delete("/{client_id}")
def delete_client(client_id: UUID, db: Session = Depends(deps.get_db)):
    crud.client.remove(db=db, _id=client_id)
    return client_id
