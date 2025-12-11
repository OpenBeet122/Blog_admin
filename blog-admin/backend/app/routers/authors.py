from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/authors", tags=["authors"])


@router.get("/", response_model=List[schemas.AuthorRead])
def list_authors(db: Session = Depends(get_db)):
    return db.query(models.Author).all()


@router.post("/", response_model=schemas.AuthorRead)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    db_author = models.Author(full_name=author.full_name, email=author.email)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author
