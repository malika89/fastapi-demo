from typing import List

from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.crud.base import BaseService
from app.models.leave_type import LeaveType
from app.schemas import LeaveTypeCreate, LeaveTypeUpdate


class LeaveTypeService(BaseService[LeaveType, LeaveTypeCreate, LeaveTypeUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: LeaveTypeCreate, owner_id: int
    ) -> LeaveType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[LeaveType]:
        return (
            db.query(self.model)
            .filter(LeaveType.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


leave_type = LeaveTypeService(LeaveType)