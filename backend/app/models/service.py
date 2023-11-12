from db.base_class import Base
from sqlalchemy.orm import Mapped

# ID (Идентификатор услуги, первичный ключ)
# Название услуги
# Описание
# Стоимость


class Service(Base):
    __tablename__ = "services"
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[float]
