from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView, FormView

from chatapp.forms import SignupForm


class IndexView(TemplateView):
    template_name = 'chatapp/index.html'

class Messanger(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'chatapp/messenger.html'


class SignupView(FormView):
    template_name = 'registration/signup.html'
    form_class = SignupForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['action_url'] = reverse('signup')
        return context

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        post_obj = request.POST
        user = User.objects.create_user(username=post_obj.get('username'),
                                        email=post_obj.get('email'),
                                        password=post_obj.get('password1'))
        user.first_name = post_obj.get('first_name')
        user.last_name = post_obj.get('last_name')
        user.save()
        return HttpResponseRedirect(reverse('login'))


def get_all_logged_in_users():
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    uid_list = []

    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id', None))

    return User.objects.filter(id__in=uid_list)

def active_users_list(request):
    return render(request, 'chatapp/active_users.html', {'active_users' : get_all_logged_in_users()})