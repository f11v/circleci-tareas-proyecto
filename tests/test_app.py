from app import app

def test_index():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hola desde Flask!"}
