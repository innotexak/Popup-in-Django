from django.shortcuts import render

from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalLoginView
from .forms import CustomAuthenticationForm

class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'registration/login.html'
    success_message = 'Success: You were successfully logged in.'
    extra_context = dict(success_url=reverse_lazy('home'))

class SignUpView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('home')

    
def home(request):
    return render(request, 'base.html')