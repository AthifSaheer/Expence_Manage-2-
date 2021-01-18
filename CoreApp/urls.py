from django.urls import path
from .views import *
from .import views

urlpatterns = [
    path('', HomeView.as_view(), name="home"),

    path('income', IncomeView.as_view(), name="income"),

    #Income Branches
    path('add-income-amount', AddIncomeView.as_view(), name="addincomeamount"),
    path('manage-income', ManageIncome.as_view(), name="manageincome"),
    path('edit-manage-income/<int:pk>/', EditIncome.as_view(), name="editmanageincome"),
    path('delete-income/<int:pk>/', DeleteIncome.as_view(), name="deleteincome"),

    path('expense', ExpenseViewModel.as_view(), name="expense"),
    
    #Expense Branches
    path('add-expense-amount', AddExpenseView.as_view(), name="addexpenseamount"),
    path('manage-expense', ManageExpense.as_view(), name="manageexpense"),
    path('edit-manage-expense/<int:pk>/', EditExpense.as_view(), name="editmanageexpense"),
    path('delete-expense/<int:pk>/', DeleteExpense.as_view(), name="deleteexpense"),

    path("graph/", GraphView.as_view(), name="graph")
    ]
