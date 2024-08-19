# app/dtos.py

class DocumentDTO:
    def __init__(self, doc_type, req_id, doc_base64):
        self.doc_type = doc_type
        self.req_id = req_id
        self.doc_base64 = doc_base64

    @classmethod
    def from_json(cls, data):
        return cls(
            doc_type=data.get('doc_type'),
            req_id=data.get('req_id'),
            doc_base64=data.get('doc_base64')
        )

    def to_dict(self):
        return {
            'doc_type': self.doc_type,
            'req_id': self.req_id,
            'doc_base64': self.doc_base64
        }
