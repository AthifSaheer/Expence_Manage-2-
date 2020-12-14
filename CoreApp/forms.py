from django import forms
from .models import AddAmount, AddExpense
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class SignupForm(UserCreationForm, forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1')