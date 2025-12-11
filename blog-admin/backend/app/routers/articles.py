from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/articles", tags=["articles"])


@router.get("/", response_model=List[schemas.ArticleRead])
def list_articles(
    status: Optional[str] = Query(None),
    author_id: Optional[int] = Query(None),
    db: Session = Depends(get_db),
):
    query = db.query(models.Article)
    if status:
        query = query.filter(models.Article.status == status)
    if author_id:
        query = query.filter(models.Article.author_id == author_id)
    return query.all()


@router.post("/", response_model=schemas.ArticleRead)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    db_article = models.Article(
        title=article.title,
        text=article.text,
        status=article.status,
        author_id=article.author_id,
        category_id=article.category_id,
    )
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article
