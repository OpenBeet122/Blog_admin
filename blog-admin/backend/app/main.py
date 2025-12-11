from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from app.database import Base, engine
from app.routers import authors, categories, articles, comments, summary
from app import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog Admin API")

app.include_router(authors.router)
app.include_router(categories.router)
app.include_router(articles.router)
app.include_router(comments.router)
app.include_router(summary.router)

app.mount("/static", StaticFiles(directory="app/frontend"), name="static")


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse("/static/index.html")
