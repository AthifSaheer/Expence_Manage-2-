from django import forms
from .models import AddAmount, AddExpense

class AddAmountForm(forms.ModelForm):
    category : forms.ChoiceField()
    
    class Meta:
        model = AddAmount
        fields = ["title", "amount", "category",]

        widgets = {
            "title" : forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Title",
            }),
            "amount" : forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Amount",
            }),
        }

class AddExpenseForm(forms.ModelForm):
    category : forms.ChoiceField()

    class Meta:
        model = AddExpense
        fields = ["title", "amount", "category"]

        widgets = {
            "title" : forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Title",
            }),
            "amount" : forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Amount",
            }),
        }
