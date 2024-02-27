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
def read_employees(
    request: Request,
    db: Session = Depends(deps.get_db),
):
    db_employees = crud.employee.get_multi(db=db)
    employees = []
    for db_employee in db_employees:
        employee = schemas.EmployeeTemplate.from_orm(db_employee).model_dump()
        employees.append(employee)
    return templates.TemplateResponse(
        request=request, name="employees.html", context={"employees": employees}
    )


@router.post("/", response_model=schemas.Employee)
def create_employee(
    employee_in: schemas.EmployeeCreate,
    db: Session = Depends(deps.get_db),
):
    try:
        employee_in.id = uuid4()
        employee = crud.employee.create(db=db, obj_in=employee_in)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    return employee


@router.post("/multi", response_model=list[schemas.Employee])
def create_employees(
    employees_in: list[schemas.EmployeeCreate],
    db: Session = Depends(deps.get_db),
):
    for employee_in in employees_in:
        try:
            employee_in.id = uuid4()
            employee = crud.employee.create(db=db, obj_in=employee_in)
            db.commit()
        except Exception as e:
            db.rollback()
            print(e)
    return employees_in


@router.put("/{employee_id}", response_model=schemas.Employee)
def update_employee(
    employee_id: UUID,
    employee_in: schemas.EmployeeUpdate,
    db: Session = Depends(deps.get_db),
):
    try:
        employee = crud.employee.update(db=db, obj_in=employee_in, _id=employee_id)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    return employee


@router.delete("/")
def delete_employee(employee_id: UUID, db: Session = Depends(deps.get_db)):
    crud.employee.remove(db=db, _id=employee_id)
    return employee_id
