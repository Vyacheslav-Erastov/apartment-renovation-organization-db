from app.crud.crud_base import CRUDBase
from app import schemas
from app import models


class CRUDOrder(CRUDBase[models.Order, schemas.OrderCreate, schemas.OrderUpdate]):
    pass


order = CRUDOrder(models.Order)
