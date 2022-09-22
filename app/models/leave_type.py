from typing import TYPE_CHECKING
from sqlalchemy import Column, ForeignKey, Integer, String,BOOLEAN
from sqlalchemy.orm import relationship

from app.database.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class LeaveType(Base):
    __tablename__ =' leave_type'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    has_common = Column(BOOLEAN)
    # provider_id = Column(Integer, ForeignKey('adm.ProviderProfile'))
    # provider = relationship("adm.ProviderProfile", back_populates="items")
    has_indefinite = Column(BOOLEAN)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['id']