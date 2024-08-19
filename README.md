# **Assignment - OCR**

The task is to develop Python-based OCR (Optical Character Recognition) API that processes images or PDFs and returns
extracted text.
  
You will be provided with the boilerplate code that contains basic application setup, API endpoints and docker-based
containerization code.

Also, you can import the provided Postman collection totest the APIs.

## **Prerequisites**

- **Docker**: Ensure Docker is installed on your system.
- **Postman**: For testing the API.

## **Setup Instructions**

### 1. **Clone the Repository**

First, clone the repository to your local machine:
```bash
git clone <repository-url>
cd <repository-directory>
```


### 2. Build and Start the Docker Containers

Use the following command to build and start the Docker containers:
```bash
docker-compose up --build
```

This will build the necessary Docker images and start the containers for the OCR API.

### 3. **Test the API**

Once the containers are running, you can test the API using Postman:

- Open Postman.
- Import the KONNECTOCRASSIGNMENT.postman_collection.json file from the root directory of the project.
- Use the imported collection to send requests to the API. The API is designed to accept a file (image or PDF) as input
  and return the OCR results.

## **API Usage**

- **Endpoint**: `POST /ocr/file-based`
- **Request**: Send a `POST` request with a file (image or PDF) in the `form-data` field named `file`.
- **Response**: JSON object containing the extracted text.


### **Sample cURL:**

```bash
curl --location 'http://127.0.0.1:8043/v1/ocr/file-based' \
--form 'document_type=@"path/to/file"' \
--form 'is_front="true"' \
--form 'document_type="AADHAR"'
```

### **Request Parameters**

| **Parameter**   | **Value**      | **Description**                                                                                             |
|-----------------|----------------|-------------------------------------------------------------------------------------------------------------|
| `document`      | `path/to/file` | The path to the file to be processed by OCR.                                                                |
| `is_front`      | `true`         | Indicates if the document is the front side.                                                                |
| `document_type` | `AADHAAR`      | Specifies the type of document being processed  (e.g., AADHAAR, PAN, DRIVING_LICENSE, PASSPORT or VOTER_ID) |


### **Multiple Versions for Approach Comparison**

We’ve provided different API endpoints like `/<version>/<path>`, allowing you to compare various approaches in your OCR implementation:

- **v1**: Uses OCR with YOLO for more advanced object detection and recognition.

- **v2**: Implements a basic OCR library for straightforward text extraction.

- **v3**: Explores another method (specify what this approach is) for further comparison.

### **Response**

### **Response Fields**

| **Field**           | **Description**                                                                                         |
|---------------------|---------------------------------------------------------------------------------------------------------|
| **documentType**    | Specifies the type of document (DL, Voter ID, Aadhar, PAN).                                             |
| **confidenceScore** | Represents the confidence score of the OCR result, which you can set based on your OCR engine's output. |
| **payload**         | The details extracted from the document                                                                 |
| **statusCode**      | Indicates the success of the API call.                                                                  |
| **statusMessage**   | Provides additional information about the success or failure of the API call.                           |

### **Sample Response**

Here are few sample "**happy case**" responses for each document type like Aadhaar, Driving License (DL), Voter ID, Aadhaar and
PAN. You can modify these responses if you want to provide more information in the response.


### **1. Driving License (DL) Response**

```json
{
  "body": {
    "errors": [],
    "response": {
      "documentType": "Driving License",
      "confidenceScore": "0.98",
      "details": {
        "documentType": "Driving License",
        "documentNumber": "DL-0420201234567",
        "name": "Rahul Sharma",
        "fatherName": "Amit Sharma",
        "dob": "1985-07-15",
        "doi": "2015-07-15",
        "doe": "2025-07-15",
        "gender": "Male",
        "mobile": "9876543210",
        "address": {
          "line1": "Flat No. 101, Green Heights",
          "line2": "Sector 62",
          "line3": "",
          "city": "Noida",
          "district": "Gautam Buddh Nagar",
          "state": "Uttar Pradesh",
          "country": "India",
          "pincode": "201301"
        },
        "photo": "https://example.com/photos/rahul_dl.jpg",
        "ageBand": null,
        "signature": "https://example.com/signatures/rahul_dl.png"
      }
    }
  },
  "status": {
    "statusCode": 200,
    "statusMessage": "OK"
  }
}
```

### **2. Voter ID Response**

```json
{
  "body": {
    "errors": [],
    "response": {
      "documentType": "Voter ID",
      "confidenceScore": "0.96",
      "details": {
        "documentType": "Voter ID",
        "documentNumber": "UP/08/098/123456",
        "name": "Priya Singh",
        "fatherName": "Rajesh Singh",
        "dob": "1992-03-21",
        "doi": "2012-03-21",
        "doe": null,
        "gender": "Female",
        "mobile": "9123456789",
        "address": {
          "line1": "House No. 22, Ashok Nagar",
          "line2": "Near Shiv Mandir",
          "line3": "",
          "city": "Lucknow",
          "district": "Lucknow",
          "state": "Uttar Pradesh",
          "country": "India",
          "pincode": "226010"
        },
        "photo": "https://example.com/photos/priya_voter.jpg",
        "ageBand": null,
        "signature": null
      }
    }
  },
  "status": {
    "statusCode": 200,
    "statusMessage": "OK"
  }
}
```

### **3. Aadhaar Response**

```json
{
  "body": {
    "errors": [],
    "response": {
      "documentType": "Aadhaar",
      "confidenceScore": "0.99",
      "details": {
        "documentType": "Aadhar",
        "documentNumber": "1234 5678 9012",
        "name": "Arun Kumar",
        "fatherName": null,
        "dob": "1990-11-05",
        "doi": null,
        "doe": null,
        "gender": "Male",
        "mobile": "9988776655",
        "address": {
          "line1": "B-45, Sector 21",
          "line2": "Gandhi Marg",
          "line3": "",
          "city": "New Delhi",
          "district": "New Delhi",
          "state": "Delhi",
          "country": "India",
          "pincode": "110001"
        },
        "photo": "https://example.com/photos/arun_aadhar.jpg",
        "ageBand": "30-40",
        "signature": null
      }
    }
  },
  "status": {
    "statusCode": 200,
    "statusMessage": "OK"
  }
}
```

### **4. PAN Response**

```json
{
  "body": {
    "errors": [],
    "response": {
      "documentType": "PAN",
      "confidenceScore": "0.97",
      "details": {
        "documentType": "PAN",
        "documentNumber": "ABCDE1234F",
        "name": "Vikram Mehta",
        "fatherName": "Suresh Mehta",
        "dob": "1988-08-09",
        "doi": null,
        "doe": null,
        "gender": "Male",
        "mobile": "9876543210",
        "address": {
          "line1": "12, Park Avenue",
          "line2": "Vile Parle",
          "line3": "",
          "city": "Mumbai",
          "district": "Mumbai Suburban",
          "state": "Maharashtra",
          "country": "India",
          "pincode": "400057"
        },
        "photo": "https://example.com/photos/vikram_pan.jpg",
        "ageBand": null,
        "signature": "https://example.com/signatures/vikram_pan.png"
      }
    }
  },
  "status": {
    "statusCode": 200,
    "statusMessage": "OK"
  }
}
```


