from django.contrib import admin
from .models import Budget, Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("title", "amount", "category", "spent_on")
    list_filter = ("category", "spent_on")
    search_fields = ("title", "notes")

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ("category", "month", "limit_amount")
    list_filter = ("category", "month")
