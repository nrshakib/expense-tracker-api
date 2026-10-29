from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Expense(models.Model):
    date = models.DateField()
    purpose = models.CharField(max_length=100, blank=True, default="")
    amount = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(0.00)])

    def __str__(self):
        return self.purpose