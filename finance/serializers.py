from rest_framework import serializers
from .models import Budget, Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = "__all__"
        read_only_fields = ("id", "created_at")
