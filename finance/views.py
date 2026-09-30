from datetime import date
from decimal import Decimal

from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Budget, Expense
from .serializers import BudgetSerializer, ExpenseSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ("category", "spent_on")
    search_fields = ("title", "category", "notes")
    ordering_fields = ("amount", "spent_on", "created_at", "category")
    ordering = ("-spent_on", "-created_at")

class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ("category", "month")
    ordering_fields = ("month", "category", "limit_amount")
    ordering = ("-month", "category")

class MonthlySummaryView(APIView):
    def get(self, request):
        try:
            year = int(request.query_params.get("year", date.today().year))
            month = int(request.query_params.get("month", date.today().month))
            month_start = date(year, month, 1)
        except (TypeError, ValueError):
            return Response({"detail": "Provide a valid year and month."}, status=status.HTTP_400_BAD_REQUEST)

        month_end = date(year + 1, 1, 1) if month == 12 else date(year, month + 1, 1)
        expenses = Expense.objects.filter(spent_on__gte=month_start, spent_on__lt=month_end)
        total = expenses.aggregate(total=Sum("amount"))["total"] or Decimal("0.00")
        category_totals = expenses.values("category").annotate(total=Sum("amount")).order_by("category")
        overall_budget = Budget.objects.filter(category="overall", month=month_start).first()

        return Response({
            "year": year,
            "month": month,
            "total_spent": f"{total:.2f}",
            "category_breakdown": {row["category"]: f"{row["total"]:.2f}" for row in category_totals},
            "overall_budget": f"{overall_budget.limit_amount:.2f}" if overall_budget else None,
        })
