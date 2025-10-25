"""Users endpoints"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

@router.get("/")
async def list_users(db: Session = Depends(get_db)):
    return []

@router.get("/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return {"id": user_id}
