from django.db import models

class Expense(models.Model):
    class Category(models.TextChoices):
        FOOD = "food", "Food"
        TRANSPORT = "transport", "Transport"
        HOUSING = "housing", "Housing"
        BILLS = "bills", "Bills"
        HEALTH = "health", "Health"
        EDUCATION = "education", "Education"
        SHOPPING = "shopping", "Shopping"
        OTHER = "other", "Other"

    title = models.CharField(max_length=160)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.OTHER)
    spent_on = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-spent_on", "-created_at"]

    def __str__(self):
        return f"{self.title} ({self.amount})"

class Budget(models.Model):
    category = models.CharField(max_length=20, default="overall")
    month = models.DateField(help_text="Use the first day of the budget month.")
    limit_amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-month", "category"]
        constraints = [
            models.UniqueConstraint(fields=["category", "month"], name="unique_budget_category_month"),
        ]

    def __str__(self):
        return f"{self.category} budget for {self.month}: {self.limit_amount}"
