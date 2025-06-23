import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_article():
    response = client.post(
        "/api/v1/articles/",
        json={
            "title": "Test Article",
            "content": "This is a test article content",
            "author": "Test Author"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Article"
    assert data["content"] == "This is a test article content"
    assert data["author"] == "Test Author"
    assert "id" in data
    return data["id"]

def test_get_article():
    article_id = test_create_article()
    response = client.get(f"/api/v1/articles/{article_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Article"

def test_list_articles():
    test_create_article()
    response = client.get("/api/v1/articles/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert isinstance(data, list)

def test_update_article():
    article_id = test_create_article()
    response = client.put(
        f"/api/v1/articles/{article_id}",
        json={
            "title": "Updated Title",
            "content": "Updated content"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"
    assert data["content"] == "Updated content"

def test_delete_article():
    article_id = test_create_article()
    response = client.delete(f"/api/v1/articles/{article_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Article deleted successfully"
    
    # Verify article is deleted
    response = client.get(f"/api/v1/articles/{article_id}")
    assert response.status_code == 404 