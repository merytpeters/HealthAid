from app import create_app, db
import pytest

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_pill_reminder(client):
    response = client.get('/pill-reminder-endpoint')
    assert response.status_code == 200
    assert b"expected_response" in response.data
