from django.contrib import admin
from .models import *

class Amount(admin.ModelAdmin):
    list_display = ('title', 'category', 'amount', 'date')

class ExpnsAmount(admin.ModelAdmin):
    list_display = ('title', 'category', 'amount', 'date_time')

admin.site.register(AddAmount, Amount)
admin.site.register(AddExpense, ExpnsAmount)
admin.site.register([IncomeCat, ExpenseCat])
admin.site.register(Graph)