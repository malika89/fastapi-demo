from fastapi import APIRouter

from app.api.v1 import leave_type

api_router = APIRouter()
api_router.include_router(leave_type.router, prefix="/leave", tags=["leave"])
