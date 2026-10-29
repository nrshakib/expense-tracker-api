from django.contrib import admin

from expenses.models import Expense

# Register your models here.
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'purpose', 'amount']
    search_fields = ['purpose']
    list_filter = ['date']
    ordering = ['-date']
    list_per_page = 20