from typing import Optional

from pydantic import BaseModel


# Shared properties
class LeaveTypeBase(BaseModel):
    name: str = None
    has_common: Optional[bool] = False
    has_indefinite: Optional[bool] = False
    # provider_id: int = None


# Properties to receive via API on creation
class LeaveTypeCreate(LeaveTypeBase):
    name: str = None
    has_common: Optional[bool] = False
    has_indefinite: Optional[bool] = False
    # provider_id: int = None


# Properties to receive via API on update
class LeaveTypeUpdate(LeaveTypeBase):
    name: Optional[str] = None


# Properties shared by models stored in DB
class LeaveTypeInDBBase(LeaveTypeBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class LeaveType(LeaveTypeInDBBase):
    pass
