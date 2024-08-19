# app/utils/utils.py

import re
import uuid
def mask_aadhar_numbers(text):
    # Regular expression pattern to find Aadhar numbers
    aadhar_pattern = r'\b(?:\d[ -]*?){12}\b'

    # Mask Aadhar numbers in the text
    masked_text = ""
    start = 0
    for match in re.finditer(aadhar_pattern, text):
        masked_text += text[start:match.start()]
        masked_text += 'X' * len(match.group()[:-4]) + match.group()[-4:]
        start = match.end()
    masked_text += text[start:]

    return masked_text


def generate_response(action, version, payload=None, request_id=None, status_code=200, status_message="OK", errors=None):
    if errors is None:
        errors = []
    if request_id is None:
        request_id = str(uuid.uuid4())
    if payload is None:
        payload = {}

    response = {
        "status": {
            "statusCode": status_code,
            "statusMessage": status_message
        },
        "body": {
            "response": payload,
            "errors": errors
        }
    }

    return response
