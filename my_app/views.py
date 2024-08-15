
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from my_app.forms import ResumeCreateForm, VacancyCreateForm
from my_app.models import Vacancy, Rezume




class IndexView(TemplateView):
    template_name = 'vacancy/index.html'

class MainView(TemplateView):
    template_name = 'vacancy/main.html'

class VacancyListView(ListView):
    model = Vacancy
    template_name = 'vacancy/vacancy_list.html'
    context_object_name = 'vacancy'

class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'vacancy/vacancy_detail.html'
    context_object_name = 'vacancy_detail'

class RezumeCreateView(CreateView):
    model = Rezume
    template_name = 'rezume/resume_create.html'
    form_class = ResumeCreateForm
    success_url = reverse_lazy('index')

class RezumeUpdateView(UpdateView):
    model = Rezume
    template_name = 'rezume/resume_create.html'
    form_class = ResumeCreateForm
    success_url = reverse_lazy('index')


class RezumeDeleteView(DeleteView):
    model = Rezume
    template_name = 'rezume/rezume_delete.html'
    success_url = reverse_lazy('index')


class RezumeListView(ListView):
    model = Rezume
    template_name = 'rezume/rezume_list.html'
    context_object_name = 'rezume'
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.role.name_en == 'admin'

    def get(self, request, *args, **kwargs):
        if not self.test_func():
            raise Http404()
        return super().get(request, *args, **kwargs)

class VacancyCreateView(CreateView):
    model = Vacancy
    template_name = 'vacancy/vacancy_create.html'
    form_class = VacancyCreateForm
    success_url = reverse_lazy('vacancy_view')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.role.name_en == 'admin'

    def get(self, request, *args, **kwargs):
        if not self.test_func():
            raise Http404()
        return super().get(request, *args, **kwargs)

class VacancyUpdateView(UpdateView):
    model = Vacancy
    template_name = 'vacancy/vacancy_update.html'
    form_class = VacancyCreateForm
    success_url = reverse_lazy('vacancy_view')
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.role.name_en == 'admin'

    def get(self, request, *args, **kwargs):
        if not self.test_func():
            raise Http404()
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return Vacancy.objects.get(pk=pk)


class VacancyDeleteView(DeleteView):
    model = Vacancy
    template_name = 'vacancy/vacancy_delete.html'
    success_url = reverse_lazy('vacancy_view')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.role.name_en == 'admin'

    def get(self, request, *args, **kwargs):
        if not self.test_func():
            raise Http404()
        return super().get(request, *args, **kwargs)
    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return Vacancy.objects.get(pk=pk)

