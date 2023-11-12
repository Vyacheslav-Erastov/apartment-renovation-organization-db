from app.crud.crud_base import CRUDBase
from app import schemas
from app import models


class CRUDWork(CRUDBase[models.Work, schemas.WorkCreate, schemas.WorkUpdate]):
    pass


work = CRUDWork(models.Work)
