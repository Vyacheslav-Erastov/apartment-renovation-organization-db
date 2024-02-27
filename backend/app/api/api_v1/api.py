from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.api.api_v1.endpoints import clients, orders, employees, services, works

api_router = APIRouter()
api_router.include_router(clients.router, prefix="/clients", tags=["clients"])
api_router.include_router(orders.router, prefix="/orders", tags=["orders"])
api_router.include_router(employees.router, prefix="/employees", tags=["employees"])
api_router.include_router(services.router, prefix="/services", tags=["services"])
api_router.include_router(works.router, prefix="/works", tags=["works"])

templates = Jinja2Templates(directory="templates")


@api_router.get("/")
def read_main(request: Request):
    return templates.TemplateResponse(request=request, name="base.html")
