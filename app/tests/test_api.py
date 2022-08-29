from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_item():
    response = client.get('/api/v1/figure', params={'lat': 90, 'lon': 180, 'type': 'sphere'})
    assert response.status_code == 200


def test_create_item():
    data = {
        "norm": [
            0,
            0,
            0
        ],
        "radius": 2,
        "color": "#AA0000",
        "lon": 180,
        "type": "sphere",
        "lat": 90
    }
    response = client.post('/api/v1/figure', json=data)
    assert response.status_code == 200
    assert 'data' in response.json()
