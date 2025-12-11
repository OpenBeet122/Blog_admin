from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.database import get_db
from app.schemas import ContentManagementRow, AuthorActivityRow

router = APIRouter(prefix="/summary", tags=["summary"])


@router.get("/content-management", response_model=List[ContentManagementRow])
def content_management(db: Session = Depends(get_db)):
    sql = text(
        '''
        SELECT
            a.title AS article_title,
            au.full_name AS author_full_name,
            c.name AS category_name,
            a.status AS status
        FROM articles a
        JOIN authors au ON a.author_id = au.id
        JOIN categories c ON a.category_id = c.id
        ORDER BY a.created_at DESC
        '''
    )
    result = db.execute(sql).mappings().all()
    return [ContentManagementRow(**row) for row in result]


@router.get("/author-activity", response_model=List[AuthorActivityRow])
def author_activity(db: Session = Depends(get_db)):
    """
    Сводный отчёт "Активность авторов":
    ФИО автора, количество опубликованных статей, общее количество комментариев.
    """
    sql = text(
        """
        SELECT
            au.full_name AS author_full_name,
            COUNT(DISTINCT CASE WHEN a.status = 'Опубликовано' THEN a.id END) AS published_articles,
            COUNT(c.id) AS total_comments
        FROM authors au
        LEFT JOIN articles a ON a.author_id = au.id
        LEFT JOIN comments c ON c.article_id = a.id
        GROUP BY au.id, au.full_name
        ORDER BY au.full_name
        """
    )
    result = db.execute(sql).mappings().all()

    return [
        AuthorActivityRow(
            author_full_name=row["author_full_name"],
            published_articles=row["published_articles"] or 0,
            total_comments=row["total_comments"] or 0,
        )
        for row in result
    ]

