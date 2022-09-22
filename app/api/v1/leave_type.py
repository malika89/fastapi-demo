from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas, crud
from app.api.deps import get_db

router = APIRouter()


@router.get("", response_model=List[schemas.LeaveType])
async def read_leave_types(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    """
    Retrieve all leave_types.
    """
    leave_types = crud.leave_type.get_multi(db, skip=skip, limit=limit)
    return leave_types


@router.post("", response_model=schemas.LeaveType)
async def create_leave_type(*, db: Session = Depends(get_db), leave_type_in: schemas.LeaveTypeCreate) -> Any:
    """
    Create new leave_types.
    """
    leave_type = crud.leave_type.create(db, obj_in=leave_type_in)
    return leave_type


@router.put("", response_model=schemas.LeaveType)
async def update_leave_type(*, db: Session = Depends(get_db), leave_type_in: schemas.LeaveTypeUpdate) -> Any:
    """
    Update existing leave_types.
    """
    leave_type = crud.leave_type.get(db, model_id=leave_type_in.id)
    if not leave_type:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The leave_type with this ID does not exist in the system.",
        )
    leave_type = crud.leave_type.update(db, db_obj=leave_type, obj_in=leave_type_in)
    return leave_type


@router.delete("", response_model=schemas.LeaveType)
async def delete_leave_type(*, db: Session = Depends(get_db), id: int) -> Any:
    """
    Delete existing leave_type.
    """
    leave_type = crud.leave_type.get(db, model_id=id)
    if not leave_type:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The leave_type with this ID does not exist in the system.",
        )
    crud.leave_type.remove(db, model_id=leave_type.id)
    return {"message": f"leave_type with ID = {id} deleted."}
