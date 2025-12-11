from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/comments", tags=["comments"])


@router.get("/", response_model=List[schemas.CommentRead])
def list_comments(
    article_id: Optional[int] = Query(None),
    db: Session = Depends(get_db),
):
    query = db.query(models.Comment)
    if article_id:
        query = query.filter(models.Comment.article_id == article_id)
    return query.all()


@router.post("/", response_model=schemas.CommentRead)
def create_comment(comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    db_comment = models.Comment(
        article_id=comment.article_id,
        author_name=comment.author_name,
        text=comment.text,
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
