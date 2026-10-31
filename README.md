# Expense Tracker API

A RESTful Expense Tracker API built with **Django** and **Django REST Framework (DRF)**. This project is part of my backend development learning journey, where I am practicing API development, CRUD operations, serializers, request validation, and HTTP responses.

## Project Status

**Current status:** Basic CRUD operations implemented. Filtering, searching, and additional improvements are planned.

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite (Django's default database, unless configured otherwise)
- Postman for API testing

## Implemented Features

- Create a new expense
- Retrieve all expenses
- Retrieve a single expense by its ID
- Partially update an expense using `PATCH`
- Fully update an expense using `PUT`
- Delete an expense
- Validate incoming data through a DRF `ModelSerializer`
- Use `get_object_or_404()` to return a `404 Not Found` response when an expense does not exist
- Manage expenses through Django Admin
- Validate that the expense amount is at least `0.01`
- Use a consistent JSON response for update and delete operations
- [ ] Filter expenses by date
- [ ] Search expenses by purpose
- [ ] Filter expenses by minimum or maximum amount
- [ ] Validation while filterng data based on query parameter
- [ ] Ordering or sorting data based on query parameter

## Expense Fields

Each expense currently contains the following fields:

| Field     | Type    | Description                                     |
| --------- | ------- | ----------------------------------------------- |
| `id`      | Integer | Automatically generated unique identifier       |
| `date`    | Date    | Date of the expense                             |
| `purpose` | String  | Purpose or description of the expense; optional |
| `amount`  | Decimal | Expense amount; must be at least `0.01`         |

## API Endpoints

The examples below assume the project is running locally at `http://127.0.0.1:8000/`.

| Method   | Endpoint                     | Description                 |
| -------- | ---------------------------- | --------------------------- |
| `POST`   | `/api/expenses/`             | Create an expense           |
| `GET`    | `/api/expenses/`             | Retrieve all expenses       |
| `GET`    | `/api/expenses/<id>/`        | Retrieve an expense by ID   |
| `PATCH`  | `/api/expenses/edit/<id>/`   | Partially update an expense |
| `PUT`    | `/api/expenses/update/<id>/` | Fully update an expense     |
| `DELETE` | `/api/expenses/delete/<id>/` | Delete an expense           |

### Example: Create an Expense

**Request**

```http
POST /api/expenses/
Content-Type: application/json
```

```json
{
  "date": "2026-10-29",
  "purpose": "Lunch",
  "amount": "150.00"
}
```

### Example: Partially Update an Expense

**Request**

```http
PATCH /api/expenses/1/
Content-Type: application/json
```

```json
{
  "amount": "200.00"
}
```

Because this endpoint uses partial updates, you only need to send the fields you want to change.

### Example: Delete an Expense

```http
DELETE /api/expenses/1/
```

The current implementation returns a success message after deletion.

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <your-project-directory>
```

Replace the placeholders with your actual GitHub repository URL and project directory.

### 2. Create and activate a virtual environment

**Windows PowerShell**

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

If you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Otherwise, install the core packages:

```bash
pip install django djangorestframework
```

### 4. Apply database migrations

```bash
py manage.py migrate
```

### 5. Start the development server

```bash
py manage.py runserver
```

The API should now be available at `http://127.0.0.1:8000/`.

> **Note:** These instructions assume your Django project uses `manage.py` and that the URL configuration matches the endpoints documented above. Adjust the commands or paths if your project structure differs.

## Testing the API

I use **Postman** to test the endpoints.

1. Start the Django development server.
2. Send requests to the endpoints listed above.
3. Check response data and HTTP status codes.
4. Test an invalid or non-existent expense ID to verify error handling.

## Planned Features

The following features are planned for future development and are **not yet implemented**:

- [ ] Improve response consistency across all endpoints
- [ ] Add automated API tests
- [ ] Add expense summaries, such as total spending

## Learning Goals

Through this project, I am practicing:

- Django models and database queries
- DRF `APIView` and HTTP methods
- `ModelSerializer` for serialization and validation
- The difference between reading existing objects and validating incoming data
- Full and partial updates
- HTTP status codes and error handling
- Testing REST APIs with Postman
- Documenting a project for GitHub

## Contributing

This is a learning project. Suggestions and feedback are welcome.
