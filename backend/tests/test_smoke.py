import django


def test_django_boots():
    """Verify Django can initialize without errors."""
    django.setup()


def test_health_endpoint(client):
    """Verify /api/health/ returns 200."""
    response = client.get("/api/health/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
