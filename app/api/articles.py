from fastapi import APIRouter, HTTPException, Depends
from typing import List
from uuid import UUID
from datetime import datetime

from app.models.article import Article, ArticleCreate, ArticleUpdate

router = APIRouter()

# In-memory storage for articles
articles_db = {}

@router.post("/", response_model=Article)
async def create_article(article: ArticleCreate):
    new_article = Article(**article.dict())
    articles_db[str(new_article.id)] = new_article
    return new_article

@router.get("/", response_model=List[Article])
async def list_articles():
    return list(articles_db.values())

@router.get("/{article_id}", response_model=Article)
async def get_article(article_id: str):
    if article_id not in articles_db:
        raise HTTPException(status_code=404, detail="Article not found")
    return articles_db[article_id]

@router.put("/{article_id}", response_model=Article)
async def update_article(article_id: str, article_update: ArticleUpdate):
    if article_id not in articles_db:
        raise HTTPException(status_code=404, detail="Article not found")
    
    stored_article = articles_db[article_id]
    update_data = article_update.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(stored_article, field, value)
    
    stored_article.updated_at = datetime.utcnow()
    articles_db[article_id] = stored_article
    return stored_article

@router.delete("/{article_id}")
async def delete_article(article_id: str):
    if article_id not in articles_db:
        raise HTTPException(status_code=404, detail="Article not found")
    del articles_db[article_id]
    return {"message": "Article deleted successfully"} 