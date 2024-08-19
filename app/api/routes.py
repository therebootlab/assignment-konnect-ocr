# app/api/routes.py

from app.utils.utils import generate_response
from flask import Blueprint, jsonify, request
from app.services.ocr_service import OCRService


api_bp = Blueprint('api', __name__)

@api_bp.route('/v1/ocr/file-based', methods=['POST'])
def ocr1():
    try:
        # Extract parameters from the request
        document_type = request.form.get('document_type', '')
        is_front = request.form.get('is_front', '')

        if 'file' not in request.files:
            errors = [{'message': 'No file part'}]
            response = generate_response(
                action="OCR_REQUEST",
                version="v1",
                status_code=400,
                status_message="Bad Request",
                errors=errors
            )
            return jsonify(response), 400

        file = request.files['file']
        if file.filename == '':
            errors = [{'message': 'No selected file'}]
            response = generate_response(
                action="OCR_REQUEST",
                version="v1",
                status_code=400,
                status_message="Bad Request",
                errors=errors
            )
            return jsonify(response), 400

        if file:
            # Call OCR service
            aadhar_info = OCRService.perform_ocr(file=file, document_type=document_type, is_front=is_front)
            # Check if aadhar_info is not None
            if aadhar_info:
                response = generate_response(
                    action="OCR_REQUEST",
                    version="v1",
                    payload=aadhar_info
                )
                return jsonify(response), 200
            else:
                errors = [{'message': 'Failed to extract information'}]
                response = generate_response(
                    action="OCR_REQUEST",
                    version="v1",
                    status_code=500,
                    status_message="Internal Server Error",
                    errors=errors
                )
                return jsonify(response), 500

    except Exception as e:
        errors = [{'message': str(e)}]
        response = generate_response(
            action="OCR_REQUEST",
            version="v1",
            status_code=500,
            status_message="Internal Server Error",
            errors=errors
        )
        return jsonify(response), 500

    @api_bp.route('/v2/ocr/file-based', methods=['POST'])
    def ocr2():
        try:
            # Extract parameters from the request
            document_type = request.form.get('document_type', '')
            is_front = request.form.get('is_front', '')

            if 'file' not in request.files:
                errors = [{'message': 'No file part'}]
                response = generate_response(
                    action="OCR_REQUEST",
                    version="v1",
                    status_code=400,
                    status_message="Bad Request",
                    errors=errors
                )
                return jsonify(response), 400

            file = request.files['file']
            if file.filename == '':
                errors = [{'message': 'No selected file'}]
                response = generate_response(
                    action="OCR_REQUEST",
                    version="v1",
                    status_code=400,
                    status_message="Bad Request",
                    errors=errors
                )
                return jsonify(response), 400

            if file:
                # Call OCR service
                aadhar_info = OCRService.perform_ocr(file=file, document_type=document_type, is_front=is_front)
                # Check if aadhar_info is not None
                if aadhar_info:
                    response = generate_response(
                        action="OCR_REQUEST",
                        version="v1",
                        payload=aadhar_info
                    )
                    return jsonify(response), 200
                else:
                    errors = [{'message': 'Failed to extract information'}]
                    response = generate_response(
                        action="OCR_REQUEST",
                        version="v1",
                        status_code=500,
                        status_message="Internal Server Error",
                        errors=errors
                    )
                    return jsonify(response), 500

        except Exception as e:
            errors = [{'message': str(e)}]
            response = generate_response(
                action="OCR_REQUEST",
                version="v1",
                status_code=500,
                status_message="Internal Server Error",
                errors=errors
            )
            return jsonify(response), 500

@api_bp.route('/v3/ocr/file-based', methods=['POST'])
def ocr3():
    try:
        # Extract parameters from the request
        document_type = request.form.get('document_type', '')
        is_front = request.form.get('is_front', '')

        if 'file' not in request.files:
            errors = [{'message': 'No file part'}]
            response = generate_response(
                action="OCR_REQUEST",
                version="v1",
                status_code=400,
                status_message="Bad Request",
                errors=errors
            )
            return jsonify(response), 400

        file = request.files['file']
        if file.filename == '':
            errors = [{'message': 'No selected file'}]
            response = generate_response(
                action="OCR_REQUEST",
                version="v1",
                status_code=400,
                status_message="Bad Request",
                errors=errors
            )
            return jsonify(response), 400

        if file:
            # Call OCR service
            aadhar_info = OCRService.perform_ocr(file=file, document_type=document_type, is_front=is_front)
            # Check if aadhar_info is not None
            if aadhar_info:
                response = generate_response(
                    action="OCR_REQUEST",
                    version="v1",
                    payload=aadhar_info
                )
                return jsonify(response), 200
            else:
                errors = [{'message': 'Failed to extract information'}]
                response = generate_response(
                    action="OCR_REQUEST",
                    version="v1",
                    status_code=500,
                    status_message="Internal Server Error",
                    errors=errors
                )
                return jsonify(response), 500

    except Exception as e:
        errors = [{'message': str(e)}]
        response = generate_response(
            action="OCR_REQUEST",
            version="v1",
            status_code=500,
            status_message="Internal Server Error",
            errors=errors
        )
        return jsonify(response), 500

    @api_bp.route('/v4/ocr/file-based', methods=['POST'])
    def ocr4():
        try:
            # Extract parameters from the request
            document_type = request.form.get('document_type', '')
            is_front = request.form.get('is_front', '')

            if 'file' not in request.files:
                errors = [{'message': 'No file part'}]
                response = generate_response(
                    action="OCR_REQUEST",
                    version="v1",
                    status_code=400,
                    status_message="Bad Request",
                    errors=errors
                )
                return jsonify(response), 400

            file = request.files['file']
            if file.filename == '':
                errors = [{'message': 'No selected file'}]
                response = generate_response(
                    action="OCR_REQUEST",
                    version="v1",
                    status_code=400,
                    status_message="Bad Request",
                    errors=errors
                )
                return jsonify(response), 400

            if file:
                # Call OCR service
                aadhar_info = OCRService.perform_ocr(file=file, document_type=document_type, is_front=is_front)
                # Check if aadhar_info is not None
                if aadhar_info:
                    response = generate_response(
                        action="OCR_REQUEST",
                        version="v1",
                        payload=aadhar_info
                    )
                    return jsonify(response), 200
                else:
                    errors = [{'message': 'Failed to extract information'}]
                    response = generate_response(
                        action="OCR_REQUEST",
                        version="v1",
                        status_code=500,
                        status_message="Internal Server Error",
                        errors=errors
                    )
                    return jsonify(response), 500

        except Exception as e:
            errors = [{'message': str(e)}]
            response = generate_response(
                action="OCR_REQUEST",
                version="v1",
                status_code=500,
                status_message="Internal Server Error",
                errors=errors
            )
            return jsonify(response), 500