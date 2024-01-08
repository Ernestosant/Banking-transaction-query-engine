from fastapi.testclient import TestClient
from main import app  # import your FastAPI app

client = TestClient(app)

def test_upload_pdf_success():
    # Assume 'test.pdf' is a valid PDF file in the same directory as the test
    files = {'file': ('test.pdf', open('data.pdf', 'rb'), 'application/pdf')}
    response = client.post("/upload-pdf/", files=files)
    assert response.status_code == 200
    assert response.json() == {"filename": "resources/data.pdf"}


def test_upload_pdf_failure():
    # Sending request without file should cause failure
    response = client.post("/upload-pdf/")
    assert response.status_code == 422  # assuming 422 for validation error


def test_get_query_response_success():
    # Mock a successful query
    test_query = {"content": "Que datos seencuentran en el documento?"}
    response = client.post("/query/", json=test_query)
    assert response.status_code == 200
    # Add more assertions based on the expected structure of your response


def test_get_query_response_failure():
    # Mock a failed query due to bad input
    test_query = {}  # Empty input or other invalid structure
    response = client.post("/query/", json=test_query)
    assert response.status_code == 422  # assuming 422 for validation error
