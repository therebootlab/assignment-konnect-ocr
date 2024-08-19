# tests/test_routes.py

import json
import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

def test_process_document(client):
    data = {
        'document_type': 'AADHAR',
        'is_front': 'true'
    }
    # Assuming the file is to be uploaded as well, simulate the file upload with a test image file
    with open('/path/to/test/image.jpeg', 'rb') as img_file:
        response = client.post(
            '/ocr/file-based',
            data={
                'document_type': data['document_type'],
                'is_front': data['is_front']
            },
            content_type='multipart/form-data',
            buffered=True,
            follow_redirects=True
        )

    assert response.status_code == 200
    assert 'status' in response.json
    assert response.json['status'] == True
