from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas
from app import crud
from app.api import dependencies as deps

router = APIRouter()


@router.get("/", response_model=list[schemas.ClientDetailed])
def read_clients(
    db: Session = Depends(deps.get_db),
):
    clients = crud.client.get_multi(db=db)
    return clients


@router.post("/", response_model=schemas.Client)
def create_client(
    client_in: schemas.ClientCreate,
    db: Session = Depends(deps.get_db),
):
    try:
        client = crud.client.create(db=db, obj_in=client_in)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    return client


@router.put("/{client_id}", response_model=schemas.Client)
def update_client(
    client_id: UUID,
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


@router.delete("/")
def delete_client(client_id: UUID, db: Session = Depends(deps.get_db)):
    crud.client.remove(db=db, _id=client_id)
    return client_id
