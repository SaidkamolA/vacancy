from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.html import strip_tags
from django.views.generic import CreateView, FormView, ListView, UpdateView, DeleteView

from my_project import settings
from users.forms import LoginForm
from users.models import Role, User


class RegistrationView(CreateView):
    template_name = 'login/register.html'
    form_class = LoginForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_registration_email(user)

        return redirect(self.get_success_url())

    def send_registration_email(self, user):
        subject = 'Подтверждение регистрации'
        html_message = render_to_string('login/register_email.html', {
            'username': user.username,
        })
        plain_message = strip_tags(html_message)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        send_mail(subject, plain_message, email_from, recipient_list, html_message=html_message, fail_silently=False)

    def get_success_url(self):
        return reverse_lazy('index')

class CustomLoginView(LoginView):
    template_name = 'login/login.html'
    def get_success_url(self):
        return reverse_lazy('index')

class SignOutView(LogoutView):
    template_name = 'vacancy/index.html'



class AdminView(ListView):
    template_name = 'admin/user_list.html'
    model = User
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.select_related('role').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['roles'] = Role.objects.all()
        return context
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.role.name_en == 'admin'

    def get(self, request, *args, **kwargs):
        if not self.test_func():
            raise Http404()
        return super().get(request, *args, **kwargs)

class ChangeRoleView(UpdateView):
    model = User
    fields = ['role']
    template_name = 'admin/change_role.html'
    success_url = reverse_lazy('admin_user_list')
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.role.name_en == 'admin'

    def get(self, request, *args, **kwargs):
        if not self.test_func():
            raise Http404()
        return super().get(request, *args, **kwargs)

class DeleteUserView(DeleteView):
    model = User
    template_name = 'admin/user_delete.html'
    success_url = reverse_lazy('admin_user_list')