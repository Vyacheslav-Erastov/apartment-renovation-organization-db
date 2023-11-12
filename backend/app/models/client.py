from app.models.order import Order
from db.base_class import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

# ID (Идентификатор клиента, первичный ключ)
# Имя
# Фамилия
# Контактная информация (телефон, электронная почта)
# Адрес


class Client(Base):
    __tablename__ = "clients"
    first_name: Mapped[str]
    second_name: Mapped[str]
    phone_number: Mapped[str]
    email: Mapped[str | None] = mapped_column(default=None)
    address: Mapped[str] = mapped_column(default=None)
    orders: Mapped[list["Order"]] = relationship(cascade="all, delete-orphan")
