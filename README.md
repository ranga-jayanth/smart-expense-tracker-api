# Smart Expense Tracker API

A portfolio backend project that manages expenses, budgets, categories, and monthly spending summaries through a Django REST API.

This project is a new API-focused implementation inspired by an earlier expense-tracking class project. It is not a copy of that repository.

## Features

- Create, list, update, and delete expenses
- Categorize expenses and filter by category or date
- Create monthly overall or category budgets
- Search expenses by title, category, and notes
- Return monthly totals and category breakdowns
- Automated API tests

## Tech stack

- Python 3.12+
- Django
- Django REST Framework
- django-filter
- SQLite for local development

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py test
python manage.py runserver
```

The API is available at `http://127.0.0.1:8000/api/`.

## Endpoints

| Method | Endpoint | Purpose |
| --- | --- | --- |
| GET/POST | `/api/expenses/` | List or create expenses |
| GET/PATCH/DELETE | `/api/expenses/<id>/` | Manage one expense |
| GET/POST | `/api/budgets/` | List or create budgets |
| GET/PATCH/DELETE | `/api/budgets/<id>/` | Manage one budget |
| GET | `/api/summary/?year=2026&month=9` | Monthly totals and category breakdown |

## Example expense

```json
{
  "title": "Groceries",
  "amount": "1250.00",
  "category": "food",
  "spent_on": "2026-09-30",
  "notes": "Weekly groceries"
}
```

## Example summary response

```json
{
  "year": 2026,
  "month": 9,
  "total_spent": "1250.00",
  "category_breakdown": {"food": "1250.00"},
  "overall_budget": "10000.00"
}
```

## Attribution

This is an original portfolio implementation built with the official Django and Django REST Framework documentation. No third-party repository is presented as original work.

- https://docs.djangoproject.com/
- https://www.django-rest-framework.org/
- https://django-filter.readthedocs.io/

## Roadmap

- Add authentication and per-user expense ownership
- Add recurring expenses and CSV export
- Add PostgreSQL configuration through environment variables
- Add a small frontend dashboard
- Add spending alerts when a budget threshold is reached