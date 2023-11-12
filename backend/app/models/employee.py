from app.models.work import Work
from db.base_class import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

# ID (Идентификатор работника, первичный ключ)
# Имя
# Фамилия
# Должность
# Контактная информация


class Employee(Base):
    __tablename__ = "employees"
    first_name: Mapped[str]
    second_name: Mapped[str]
    job_title: Mapped[str]
    phone_number: Mapped[str]
    email: Mapped[str | None] = mapped_column(default=None)
    works: Mapped[list["Work"]] = relationship(cascade="all, delete-orphan")
