from datetime import datetime
from uuid import UUID

from sqlalchemy import ForeignKey
from app.models.order import Order
from db.base_class import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

# ID (Идентификатор работы, первичный ключ)
# ID заказа (внешний ключ, связывающий сущности Заказы)
# ID услуги (внешний ключ, связывающий сущности Услуги)
# Дата начала работы
# Дата завершения работы
# Описание работы


class Work(Base):
    __tablename__ = "works"
    start_date: Mapped[datetime]
    finish_date: Mapped[datetime | None] = mapped_column(default=None)
    description: Mapped[str | None] = mapped_column(default=None)
    service_id: Mapped[UUID] = mapped_column(ForeignKey("services.id"))
    order_id: Mapped[UUID] = mapped_column(ForeignKey("orders.id"))
