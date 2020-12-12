from django.contrib import admin
from .models import *


admin.site.register([AddAmount,  AddExpense, IncomeCat, ExpenseCat])