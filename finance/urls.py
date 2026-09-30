from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BudgetViewSet, ExpenseViewSet, MonthlySummaryView

router = DefaultRouter()
router.register("expenses", ExpenseViewSet, basename="expense")
router.register("budgets", BudgetViewSet, basename="budget")

urlpatterns = [
    path("summary/", MonthlySummaryView.as_view(), name="monthly-summary"),
] + router.urls
