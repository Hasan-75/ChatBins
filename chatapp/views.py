from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView, FormView

from chatapp.forms import SignupForm


class IndexView(TemplateView):
    template_name = 'chatapp/index.html'

class LoginView(FormView):
    template_name = 'chatapp/forms.html'
    form_class = AuthenticationForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['action_url'] = reverse('login')
        return context

    def post(self, request, *args, **kwargs):
        pass

class SignupView(FormView):
    template_name = 'chatapp/forms.html'
    form_class = SignupForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['action_url'] = reverse('signup')
        return context

    def post(self, request, *args, **kwargs):
        pass