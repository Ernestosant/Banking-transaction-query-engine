# Banking-transaction-query-engine
This project processes PDF documents with credit card transaction data to answer questions and extract data through natural language instructions.


## Description
This repository contains a FastAPI-based web application that enables the uploading of PDF files and processes queries using OpenAI GPT-4.

## Files in the Repository

- `main.py`: Contains the main code of the FastAPI application, including endpoints for uploading PDF files and performing queries.
- `test_api.py`: Contains unit tests for the FastAPI endpoints.
- `requirements.txt`: Lists all the dependencies required to run the application.
- `untils.py`: Provides helper functions for reading PDF files and making requests to GPT-4.
- `consts.py`: Contains constants used throughout the application, such as the API key and the GPT-4 model.
- `models.py`: Defines Pydantic models for validating input data.

## Installation

1. Clone the repository:
   ```
   git clone [repository URL]
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To start the FastAPI application:

```
uvicorn main:app --reload
```

This will launch a local server on port 8000.

## Endpoints

### POST /upload-pdf/
- Description: Allows uploading a PDF file.
- Input: A PDF file.
- Output: Name of the saved file.

### POST /query/
- Description: Processes a query using GPT-4 and returns a response.
- Input: `QueryRequest` object with the query content.
- Output: Response generated by GPT-4.

## Running Tests

Run the unit tests with the following command:

```
pytest test_api.py
```
**Note:** 
To run the tests, you must create a directory named `resources/data.pdf`. Where **data.pdf** is the document on which the tests will be conducted.

## Try it on Render
The API is deployed on Render. You can access the Swagger UI [here](https://transaction-query-engine.onrender.com/docs#/).
