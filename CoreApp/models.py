from django.db import models
from datetime import datetime

class IncomeCat(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.title

class ExpenseCat(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.title

class AddAmount(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(IncomeCat, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title + " | " + self.category.title

class AddExpense(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(ExpenseCat, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    date_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title + " | " + self.category.title

"""
class TotalIncome(models.Model):
    cat = models.ForeignKey(IncomeCat, on_delete=models.CASCADE)
    amount_tt = models.ForeignKey(AddAmount.amount, on_delete=models.CASCADE)"""