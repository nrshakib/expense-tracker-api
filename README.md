
# Expense Tracker API

A RESTful Expense Tracker API built with Django and Django REST Framework. This project allows users to manage expenses, filter and search records, analyze spending statistics, and generate expense reports based on date ranges.

## Features

### 1. Expense Management (CRUD)
- Create a new expense.
- Retrieve all expenses.
- Retrieve a single expense by ID.
- Update an expense using PUT or PATCH.
- Delete an expense.

### 2. Filtering and Searching
- Filter expenses by a specific date.
- Search expenses by purpose (case-insensitive).
- Filter expenses by minimum amount.
- Combine multiple filters in a single request.

### 3. Ordering
- Order expenses by date.
- Order expenses by amount.
- Order expenses by purpose.
- Support both ascending and descending order.

### 4. Expense Statistics
Retrieve overall expense statistics, including:
- Total expense amount.
- Highest expense.
- Lowest expense.
- Average expense.
- Total number of expense records.

### 5. Date-range Expense Report
Generate an expense report for a specific date range.

The report includes:
- Total expense amount.
- Highest expense.
- Lowest expense.
- Average expense.
- Total number of expenses.

Date validation includes:
- Required date parameters.
- Valid date format (`YYYY-MM-DD`).
- Start date cannot be later than end date.

### 6. Data Validation
- Serializer-based validation.
- Expense purpose must contain at least 3 characters when provided.
- Expense amount must be greater than or equal to 0.01.
- Date and query parameter validation.

### 7. Consistent API Responses

Successful API responses follow a consistent structure:

```json
{
    "message": "Data retrieved successfully",
    "status_text": "Success",
    "data": {}
}
```

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite / Configured Database
- Django ORM
- Postman

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/expenses/` | Retrieve all expenses |
| POST | `/expenses/create/` | Create an expense |
| GET | `/expenses/<id>/` | Retrieve a single expense |
| PATCH | `/expenses/edit/<id>/` | Partially update an expense |
| PUT | `/expenses/update/<id>/` | Fully update an expense |
| DELETE | `/expenses/delete/<id>/` | Delete an expense |
| GET | `/expenses/stats/` | Retrieve expense statistics |
| GET | `/expenses/report/` | Generate a date-range report |

## Query Parameters

### Filter by Date

```http
GET /expenses/?date=2026-10-29
```

### Search by Purpose

```http
GET /expenses/?search=breakfast
```

### Filter by Minimum Amount

```http
GET /expenses/?min_amount=100
```

### Order Expenses

```http
GET /expenses/?ordering=-amount
```

Supported ordering values:

- `date`
- `-date`
- `amount`
- `-amount`
- `purpose`
- `-purpose`

### Combine Filters and Ordering

```http
GET /expenses/?date=2026-10-29&min_amount=100&search=food&ordering=-amount
```

## Expense Statistics

Retrieve overall expense statistics:

```http
GET /expenses/stats/
```

Example response:

```json
{
    "message": "Statistics retrieved successfully",
    "status_text": "Success",
    "data": {
        "total_expense": 350.0,
        "max_expense": 120.0,
        "min_expense": 0.0,
        "avg_expense": 58.3333333333333,
        "expense_count": 6
    }
}
```

## Date-range Expense Report

Generate a report between two dates:

```http
GET /expenses/report/?start_date=2026-10-27&end_date=2026-10-29
```

Both dates are required and must follow the `YYYY-MM-DD` format.

## Django ORM Concepts Practiced

- `filter()`
- `exclude()`
- `get()`
- `count()`
- `exists()`
- `aggregate()`
- `Sum()`
- `Max()`
- `Min()`
- `Avg()`
- `Count()`
- `date__range`
- `date__gte`
- `date__lt`
- `amount__gte`
- `purpose__icontains`

## Installation and Setup

1. Clone the repository:

```bash
git clone <https://github.com/nrshakib/expense-tracker-api>
```

2. Navigate to the project directory:

```bash
cd expense-tracker-api
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment (Windows):

```bash
venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install django djangorestframework
```

6. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

7. Start the development server:

```bash
python manage.py runserver
```

The development server will be available at:

```text
http://127.0.0.1:8000/
```

## Testing

API endpoints and query parameters have been manually tested using Postman.

Test coverage includes:
- Expense CRUD operations.
- Serializer validation.
- Filtering and searching.
- Ordering.
- Invalid query parameter handling.
- Expense statistics.
- Date-range reports.
- Date validation and edge cases.

## Learning Objectives

This project was developed as part of a hands-on Django REST Framework learning journey.

The main objectives were:

- Understand APIView and HTTP methods.
- Implement CRUD operations using serializers.
- Work with Django ORM queries.
- Implement filtering, searching, and ordering.
- Validate query parameters and request data.
- Perform database aggregation.
- Generate expense statistics and date-range reports.
- Test REST API endpoints using Postman.

---

**Project Status:** Core Beginner Project Completed.