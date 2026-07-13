from django.contrib import admin

from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'timestamp', 'category')
    list_filter = ('category', 'timestamp')
    search_fields = ('name', 'amount', 'category')