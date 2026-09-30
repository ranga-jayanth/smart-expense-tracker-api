from datetime import date
from decimal import Decimal

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Budget, Expense

class FinanceApiTests(APITestCase):
    def test_create_expense(self):
        response = self.client.post("/api/expenses/", {
            "title": "Groceries",
            "amount": "1250.00",
            "category": "food",
            "spent_on": "2026-09-30",
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Expense.objects.first().amount, Decimal("1250.00"))

    def test_monthly_summary(self):
        Expense.objects.create(title="Food", amount=Decimal("100.00"), category="food", spent_on=date(2026, 9, 10))
        Expense.objects.create(title="Bus", amount=Decimal("50.00"), category="transport", spent_on=date(2026, 9, 12))
        Budget.objects.create(category="overall", month=date(2026, 9, 1), limit_amount=Decimal("1000.00"))
        response = self.client.get("/api/summary/?year=2026&month=9")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["total_spent"], "150.00")
        self.assertEqual(response.data["overall_budget"], "1000.00")
        self.assertEqual(response.data["category_breakdown"]["food"], "100.00")

    def test_invalid_summary_parameters(self):
        response = self.client.get("/api/summary/?year=2026&month=not-a-month")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
