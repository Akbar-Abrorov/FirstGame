from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column
from cfg.database import Base, str_uniq, int_pk, str_null_true

class Item(Base):
    id: Mapped[int_pk]
    item_name: Mapped[str_uniq]
    item_description: Mapped[str_null_true]
    count: Mapped[int] = mapped_column(server_default=text('0'))

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, item_name={self.item_name!r})"

    def __repr__(self):
        return str(self)

