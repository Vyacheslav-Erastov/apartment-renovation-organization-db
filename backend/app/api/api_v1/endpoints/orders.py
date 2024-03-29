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
def read_orders(
    request: Request,
    db: Session = Depends(deps.get_db),
):
    db_orders = crud.order.get_multi(db=db)
    orders = []
    for db_order in db_orders:
        order = schemas.OrderTemplate.from_orm(db_order).model_dump()
        orders.append(order)
    return templates.TemplateResponse(
        request=request, name="orders.html", context={"orders": orders}
    )


@router.post("/")
def create_order(
    request: Request,
    order_in: schemas.OrderCreate = Depends(schemas.OrderForm.as_form),
    db: Session = Depends(deps.get_db),
):
    try:
        order = crud.order.create(db=db, obj_in=order_in)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    return RedirectResponse(
        request.url_for("read_orders"), status_code=status.HTTP_303_SEE_OTHER
    )


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
