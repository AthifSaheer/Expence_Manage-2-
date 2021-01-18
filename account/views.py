from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView, TemplateView
from .forms import CustomSignup
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


class SignupView(FormView):
    template_name = 'registration/signup.html'
    form_class = CustomSignup
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        user = User.objects.create_user(username=username, email=email, password=password,)
        usr = form.save(commit=False)
        usr.save()
        return HttpResponseRedirect(self.get_success_url())
