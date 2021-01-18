from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from .forms import *
from .models import *

#DashBoard / Home
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        a = AddAmount.objects.filter(id=9)
        income = AddAmount.objects.all().order_by("-id")[:1]
        expense = AddExpense.objects.all().order_by("-id")[:1]
        context['add_amount'] = income
        context['expense'] = expense
        return context

class GraphView(TemplateView):
    template_name = "graph.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        a = AddAmount.objects.filter(id=9)
        income = AddAmount.objects.all()
        expense = AddExpense.objects.all()
        context['add_amount'] = income
        context['expense'] = expense
        return context


#Income View
class IncomeView(TemplateView):
    template_name = "income/income.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_amount'] = AddAmount.objects.all().order_by('-id')
        return context

#Income Branches
class AddIncomeView(CreateView):
    template_name = "income/addincome.html"
    form_class = AddAmountForm
    success_url = 'income'

    def form_valid(self, form):
        x = form.save()
        return super().form_valid(form)

class ManageIncome(TemplateView):
    template_name = "income/manageincome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_amount_db'] = AddAmount.objects.all()
        return context

class EditIncome(UpdateView):
    template_name = "income/editincome.html"
    get_object_name = "changeincome"
    model = AddAmount
    fields = ('title', 'amount', 'category')

    def get_success_url(self):
        return reverse_lazy('manageincome')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class DeleteIncome(DeleteView):
    template_name = "income/confirm_delete.html"
    model = AddAmount
    success_url = "/manage-income"

#Expense View
class ExpenseViewModel(TemplateView):
    template_name = "expense/expense.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_expense'] = AddExpense.objects.all()
        return context

#Expense Branches
class AddExpenseView(CreateView):
    template_name = "expense/addexpense.html"
    form_class = AddExpenseForm
    success_url = "expense"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ManageExpense(TemplateView):
    template_name = "expense/manageexpense.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_expense'] = AddExpense.objects.all()
        return context


class EditExpense(UpdateView):
    template_name = "expense/editexpense.html"
    get_object_name = "changeexpense"
    model = AddExpense
    fields = ("title", "amount", "category")

    def get_success_url(self):
        return reverse_lazy("manageexpense")

class DeleteExpense(DeleteView):
    template_name = "expense/confirm_delete.html"
    model = AddExpense
    success_url = "/manage-expense"
