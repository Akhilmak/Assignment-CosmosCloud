# Student Management API

This is a simple FastAPI application for managing student data, built with MongoDB as the database. The API provides endpoints for adding, updating, fetching, listing, and deleting student records, along with optional filtering.

## Features

- **Create a student**
- **List all students with optional filters** (filter by `country` or `age`)
- **Fetch a student by ID**
- **Update a student by ID**
- **Delete a student by ID**
- **Health check endpoint (HEAD request)**

## Prerequisites

- Python 3.7+
- MongoDB (hosted at MongoDB Atlas)
- FastAPI
- Uvicorn (for running the app)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Akhilmak/Assignment-CosmosCloud.git
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your MongoDB instance (local or cloud) and update the database connection in `database.py`.

## Running the Application

To run the FastAPI application locally with Uvicorn:

```bash
uvicorn main:app --host 0.0.0.0 --port 10000 --reload
```

- The `--reload` option allows automatic code reloading during development.
- Replace `0.0.0.0` with `localhost` if you don't need to run it on all network interfaces.

## API Endpoints

### 1. `POST /students/` - Create a student

Create a new student record.

**Request Body:**

```json
{
  "name": "John Doe",
  "age": 22,
  "address": {
    "city": "New York",
    "country": "USA"
  }
}
```

**Response:**

```json
{
  "id": "string"  # The ID of the newly created student
}
```

### 2. `GET /students/` - List students

Get a list of students. You can filter by `country` and/or `age`.

**Query Parameters:**

- `country` (optional) - Filter by country.
- `age` (optional) - Filter students with age greater than or equal to the provided age.

**Response:**

```json
{
  "data": [
    {
      "name": "John Doe",
      "age": 22
    },
    ...
  ]
}
```

### 3. `GET /students/{id}` - Fetch a student by ID

Fetch a student's data by their ID.

**Response:**

```json
{
  "name": "John Doe",
  "age": 22,
  "address": {
    "city": "New York",
    "country": "USA"
  }
}
```

### 4. `PATCH /students/{id}` - Update student by ID

Update a student's information. You can provide only the fields that need to be updated.

**Request Body:**

```json
{
  "name": "Jane Doe",
  "age": 23,
  "address": {
    "city": "Los Angeles",
    "country": "USA"
  }
}
```

**Response:**

- `204 No Content` - Successful update, no body content returned.

### 5. `DELETE /students/{id}` - Delete student by ID

Delete a student by their ID.

**Response:**

```json
{
  "message": "Student deleted successfully"
}
```

### 6. `HEAD /` - Health check

Check if the API is available.

**Response:**

- `200 OK` - API is available.

## Error Handling

- **404 Not Found** - When a student or resource is not found.
- **400 Bad Request** - When there is an invalid request format (e.g., invalid student ID).
- **422 Unprocessable Entity** - When required fields are missing in a request body.
- **204 No Content** - For successful updates with no response body.
