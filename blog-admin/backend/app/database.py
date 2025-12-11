import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


def get_database_url() -> str:
    user = os.getenv("MYSQL_USER", "blog_user")
    password = os.getenv("MYSQL_PASSWORD", "blog_password")
    host = os.getenv("MYSQL_HOST", "db")
    port = os.getenv("MYSQL_PORT", "3306")
    db = os.getenv("MYSQL_DB", "blog_db")

    return f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}"


DATABASE_URL = get_database_url()
engine = create_engine(DATABASE_URL, echo=False, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
