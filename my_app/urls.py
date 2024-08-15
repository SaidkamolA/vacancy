from django.urls import path
from django.views.generic import DeleteView

from my_app.views import VacancyListView, VacancyDetailView, RezumeCreateView, RezumeUpdateView, RezumeDeleteView, \
    RezumeListView, VacancyCreateView, VacancyUpdateView, VacancyDeleteView, IndexView, MainView
from users.views import RegistrationView, CustomLoginView, SignOutView, AdminView, ChangeRoleView, DeleteUserView

urlpatterns = [
    path('admin/users/', AdminView.as_view(), name='admin_user_list'),
    path('admin/users/<int:pk>/change_role/', ChangeRoleView.as_view(), name='change_role'),
    path('index/',IndexView.as_view(),name='index'),
    path('main/', MainView.as_view(), name='main'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', SignOutView.as_view(), name='logout'),
    path('vacancy_view',VacancyListView.as_view(),name='vacancy_view'),
    path('vacancy_detail/<int:pk>', VacancyDetailView.as_view(), name='vacancy_detail'),
    path('resume_create', RezumeCreateView.as_view(), name='rezume_create'),
    path('resume_update/<int:pk>', RezumeUpdateView.as_view(), name='rezume_update'),
    path('resume_delete/<int:pk>', RezumeDeleteView.as_view(), name='rezume_delete'),
    path('rezume_view', RezumeListView.as_view(), name='rezume_view'),
    path('vacancy_create', VacancyCreateView.as_view(), name='vacancy_create'),
    path('vacancy_update/<int:pk>', VacancyUpdateView.as_view(), name='vacancy_update'),
    path('vacancy_delete/<int:pk>', VacancyDeleteView.as_view(), name='vacancy_delete'),
    path('user_delete/<int:pk>', DeleteUserView.as_view(), name='delete_user'),

]
