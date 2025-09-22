import pytest
from app import app

def test_index():
    client = app.test_client()
    rv = client.get("/")
    assert rv.status_code == 200
    assert b"Use GET" in rv.data

def test_user_gists_octocat():
    client = app.test_client()
    rv = client.get("/octocat")
    assert rv.status_code == 200
    data = rv.get_json()
    assert isinstance(data, list)
    # octocat always has at least one gist
    assert "id" in data[0]
    assert "html_url" in data[0]
