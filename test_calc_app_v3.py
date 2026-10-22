from fastapi.testclient import TestClient
from calc_app_v3 import app
client = TestClient(app)


#calling root
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Microservice!"}  #exact JSON

#test multiplication
def test_calculator():
    #
    #validate 2*3=6
    response = client.client.post("/operation", json={"num1": 2, "opt" : "*", "num2": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 6.0}  

    # check if supporUI is up and running (for FastAPI)
    def test_docs():
        response = client.get("/docs")
        assert response.status_code == 200

