from app.crud.crud_base import CRUDBase
from app import schemas
from app import models


class CRUDService(
    CRUDBase[models.Service, schemas.ServiceCreate, schemas.ServiceUpdate]
):
    pass


service = CRUDService(models.Service)
