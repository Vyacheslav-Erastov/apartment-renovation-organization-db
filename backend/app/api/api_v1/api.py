from fastapi import APIRouter

from app.api.api_v1.endpoints import tasks, events, websockets

api_router = APIRouter()
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(events.router, prefix="/events", tags=["events"])
api_router.include_router(websockets.router, prefix="", tags=["websockets"])
