from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Budget",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("category", models.CharField(default="overall", max_length=20)),
                ("month", models.DateField(help_text="Use the first day of the budget month.")),
                ("limit_amount", models.DecimalField(decimal_places=2, max_digits=12)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-month", "category"], "constraints": [models.UniqueConstraint(fields=("category", "month"), name="unique_budget_category_month")]},
        ),
        migrations.CreateModel(
            name="Expense",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=160)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=12)),
                ("category", models.CharField(choices=[("food", "Food"), ("transport", "Transport"), ("housing", "Housing"), ("bills", "Bills"), ("health", "Health"), ("education", "Education"), ("shopping", "Shopping"), ("other", "Other")], default="other", max_length=20)),
                ("spent_on", models.DateField()),
                ("notes", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["-spent_on", "-created_at"]},
        ),
    ]
