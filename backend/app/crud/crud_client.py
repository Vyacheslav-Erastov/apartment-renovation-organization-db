from app.crud.crud_base import CRUDBase
from app import schemas
from app import models


class CRUDClient(CRUDBase[models.Client, schemas.ClientCreate, schemas.ClientUpdate]):
    pass


client = CRUDClient(models.Client)
