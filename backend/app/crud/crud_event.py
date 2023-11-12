from sqlalchemy.orm import Session
from app.crud.crud_base import CRUDBase
from app.models.event import Event
from app import schemas
from app.schemas.event import EventCreate
from app.core.connection_manager import manager


class CRUDEvent(CRUDBase[Event, schemas.EventCreate, schemas.EventUpdate]):
    def create(self, db: Session, obj_in: EventCreate) -> Event:
        result = super().create(db, obj_in)
        db.commit()
        manager.add_task(
            message=schemas.MessageWS(event=schemas.EventWS.EVENT_CREATE, data=obj_in)
        )
        return result


event = CRUDEvent(Event)
