from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.articles import router as articles_router

app = FastAPI(
    title="Article API",
    description="A simple CRUD API for managing articles",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(articles_router, prefix="/api/v1/articles", tags=["articles"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Article API"} 