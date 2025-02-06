# Number Classification API

## Overview
This API takes a number as input and returns various mathematical properties about it, including:

- Whether it is `prime`.
- Whether it is `a perfect number`.
- If it is an `Armstrong number`.
- Whether it is `even or odd`.
- The `sum of its digits`.
- A `fun fact` retrieved from the [Numbers API](http://numbersapi.com/).

This project is part of the **HNG12 Backend Internship - Stage 1 Task**.

## Features
- ✅ Accepts a number as a query parameter.
- ✅ Returns a structured JSON response with mathematical properties.
- ✅ Retrieves a fun fact from the Numbers API.
- ✅ Handles errors and invalid input gracefully.
- ✅ CORS-enabled for cross-origin access.
- ✅ Fast and lightweight.

## API Documentation

### Endpoint
`GET /api/classify-number?number=371`



### Example Response (200 OK)
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### Error Response (400 Bad Request)
```json
{
    "number": "abc",
    "error": true
}
```

## Installation & Setup

### 1. Clone the Repository
```sh
git clone https://github.com/zuuhair11/Hng12_Backend_S01_Number-Classification-API
cd Hng12_Backend_S01_Number-Classification-API
```

### 2. Activate Virtual Environment
```sh
# macOS/Linux
source env/bin/activate

# Windows
env\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run the API Locally
```sh
uvicorn main:app --reload
```

### 5. Test the API
Open your browser and go to:
```
http://127.0.0.1:8000/api/classify-number?number=371
```

