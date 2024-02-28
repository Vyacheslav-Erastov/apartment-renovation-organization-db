from datetime import datetime
from enum import Enum
from uuid import UUID

from sqlalchemy import ForeignKey
from app.models.work import Work
from app.db.base_class import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

# ID (Идентификатор заказа, первичный ключ)
# ID клиента (внешний ключ, связывающий сущности Клиенты)
# Дата начала ремонта
# Дата завершения ремонта
# Стоимость
# Статус заказа (в работе, завершен, отменен и т.д.)


class OrderStatus(str, Enum):
    CREATED = "CREATED"
    IN_PROGRESS = "IN_PROGRESS"
    CANCELED = "CANCELED"
    COMPLETED = "COMPLETED"


class Order(Base):
    __tablename__ = "orders"
    start_date: Mapped[datetime | None] = mapped_column(default=None)
    finish_date: Mapped[datetime] = mapped_column(default=None)
    price: Mapped[float | None] = mapped_column(default=None)
    status: Mapped[OrderStatus]
    paid: Mapped[bool] = mapped_column(default=False)
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    works: Mapped[list["Work"]] = relationship(cascade="all, delete-orphan")
