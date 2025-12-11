from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel


class AuthorBase(BaseModel):
    full_name: str
    email: str


class AuthorCreate(AuthorBase):
    pass


class AuthorRead(AuthorBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryRead(CategoryBase):
    id: int

    class Config:
        from_attributes = True


class ArticleBase(BaseModel):
    title: str
    text: str
    status: str
    author_id: int
    category_id: int


class ArticleCreate(ArticleBase):
    pass


class ArticleRead(ArticleBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class CommentBase(BaseModel):
    article_id: int
    author_name: str
    text: str


class CommentCreate(CommentBase):
    pass


class CommentRead(CommentBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ContentManagementRow(BaseModel):
    article_title: str
    author_full_name: str
    category_name: str
    status: str


class AuthorActivityRow(BaseModel):
    author_full_name: str
    published_articles: int
    total_comments: int
