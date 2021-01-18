from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

#authentication

class IncomeCat(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.title

class ExpenseCat(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.title

class AddAmount(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    category = models.ForeignKey(IncomeCat, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title + " | " + self.category.title

class AddExpense(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    category = models.ForeignKey(ExpenseCat, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    date_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title + " | " + self.category.title

class Graph(models.Model):
    income = models.ForeignKey(AddAmount, on_delete=models.CASCADE)
    expense = models.ForeignKey(AddExpense, on_delete=models.CASCADE)

    def __str__(self):
        return self.income

"""
class TotalIncome(models.Model):
    cat = models.ForeignKey(IncomeCat, on_delete=models.CASCADE)
    amount_tt = models.ForeignKey(AddAmount.amount, on_delete=models.CASCADE)"""