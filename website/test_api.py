import pytest
from website import create_app, db
from website.models import Note


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


# -------------------------
# CREATE
# -------------------------
def test_create_note(client):
    response = client.post('/api/notes', json={
        "data": "pytest note"
    })

    assert response.status_code == 201

    data = response.get_json()
    assert "id" in data
    assert data["data"] == "pytest note"


# -------------------------
# READ ALL
# -------------------------
def test_get_all_notes(client):
    client.post('/api/notes', json={"data": "note 1"})
    client.post('/api/notes', json={"data": "note 2"})

    response = client.get('/api/notes')

    assert response.status_code == 200

    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 2


# -------------------------
# READ SINGLE
# -------------------------
def test_get_single_note(client):
    create = client.post('/api/notes', json={"data": "single note"})
    note_id = create.get_json()["id"]

    response = client.get(f'/api/notes/{note_id}')

    assert response.status_code == 200

    data = response.get_json()
    assert data["data"] == "single note"


def test_get_single_note_not_found(client):
    response = client.get('/api/notes/999')

    assert response.status_code == 404


# -------------------------
# UPDATE
# -------------------------
def test_update_note(client):
    create = client.post('/api/notes', json={"data": "old note"})
    note_id = create.get_json()["id"]

    response = client.put(f'/api/notes/{note_id}', json={
        "data": "updated note"
    })

    assert response.status_code == 200

    data = response.get_json()
    assert data["data"] == "updated note"


def test_update_note_not_found(client):
    response = client.put('/api/notes/999', json={
        "data": "nothing"
    })

    assert response.status_code == 404


# -------------------------
# DELETE
# -------------------------
def test_delete_note(client):
    create = client.post('/api/notes', json={"data": "to delete"})
    note_id = create.get_json()["id"]

    response = client.delete(f'/api/notes/{note_id}')

    assert response.status_code == 200


def test_delete_note_not_found(client):
    response = client.delete('/api/notes/999')

    assert response.status_code == 404