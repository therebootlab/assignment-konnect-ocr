
import logging

class OCRService:
    # Initialize logger
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)



    @classmethod
    def extract_identity_info(cls, ocr_result, document_type):
        details = {
            "documentType": None,  # Type of document (DL, Aadhar, PAN, Voter ID, etc.)
            "documentNumber": None,  # Generic field for ID number (DL No., Aadhar No., PAN No., Voter ID No.)
            "name": None,
            "fatherName": None,  # Field for father's name (common in PAN, Voter ID)
            "dob": None,  # Date of Birth
            "doi": None,  # Date of Issue (common in DL, Voter ID)
            "doe": None,  # Date of Expiry (common in DL)
            "gender": None,
            "mobile": None,  # Mobile number (common in Aadhar)
            "address": {
                "line1": None,
                "line2": None,
                "line3": None,
                "city": None,
                "district": None,
                "state": None,
                "country": "India",  # Default to India
                "pincode": None
            },
            "photo": None,  # Placeholder for a link to the photo (if applicable)
            "ageBand": None,  # Optional field (common in Aadhar)
            "signature": None  # Placeholder for a signature (common in DL, PAN)
        }

        response_content = {
            "documentType": document_type,
            "confidenceScore": "",
            "details": details
        }

        return response_content

    @classmethod
    def perform_ocr(cls, file, document_type, is_front):
        # Read the image and process


        # Use OCRService methods


        # Perform OCR


        # Extract Aadhar info
        aadhar_info = cls.extract_identity_info('lok', document_type)

        return aadhar_info