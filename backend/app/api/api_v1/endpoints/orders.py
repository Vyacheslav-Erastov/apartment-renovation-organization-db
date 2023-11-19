from uuid import UUID, uuid4
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas
from app import crud
from app.api import dependencies as deps

router = APIRouter()


@router.get("/", response_model=list[schemas.OrderDetailed])
def read_orders(
    db: Session = Depends(deps.get_db),
):
    orders = crud.order.get_multi(db=db)
    return orders


@router.post("/", response_model=schemas.Order)
def create_order(
    order_in: schemas.OrderCreate,
    db: Session = Depends(deps.get_db),
):
    try:
        order_in.id = uuid4()
        order = crud.order.create(db=db, obj_in=order_in)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    return order


@router.post("/multi", response_model=list[schemas.Order])
def create_orders(
    orders_in: list[schemas.OrderCreate],
    db: Session = Depends(deps.get_db),
):
    for order_in in orders_in:
        try:
            order_in.id = uuid4()
            order = crud.order.create(db=db, obj_in=order_in)
            db.commit()
        except Exception as e:
            db.rollback()
            print(e)
    return orders_in


@router.put("/{order_id}", response_model=schemas.Order)
def update_order(
    order_id: UUID,
    order_in: schemas.OrderUpdate,
    db: Session = Depends(deps.get_db),
):
    try:
        order = crud.order.update(db=db, obj_in=order_in, _id=order_id)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    return order


@router.delete("/")
def delete_order(order_id: UUID, db: Session = Depends(deps.get_db)):
    crud.order.remove(db=db, _id=order_id)
    return order_id
