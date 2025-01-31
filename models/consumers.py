from sqlalchemy.orm import  Mapped
from cfg.database import Base, str_uniq, int_pk


class Consumer(Base):
    __tablename__ = 'consumers'
    id: Mapped[int_pk]
    name: Mapped[str]
    phone_number: Mapped[str_uniq]
    course: Mapped[int]
    items_id: Mapped[str]

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"name={self.name!r}")
    def __repr__(self):
        return str(self)