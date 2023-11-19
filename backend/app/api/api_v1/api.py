from fastapi import APIRouter

from app.api.api_v1.endpoints import clients, orders, employees, services, works

api_router = APIRouter()
api_router.include_router(clients.router, prefix="/clients", tags=["clients"])
api_router.include_router(orders.router, prefix="/orders", tags=["orders"])
api_router.include_router(employees.router, prefix="/employees", tags=["employees"])
api_router.include_router(services.router, prefix="/services", tags=["services"])
api_router.include_router(works.router, prefix="/works", tags=["works"])
