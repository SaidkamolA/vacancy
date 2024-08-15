from django import forms

from my_app.models import Rezume, Vacancy


class ResumeCreateForm(forms.ModelForm):

    class Meta:
        model = Rezume
        fields = ['vacancy','name','surname','patronymic','date_of_birth','email','skills','pro_experience','education']


class VacancyCreateForm(forms.ModelForm):

    class Meta:
        model = Vacancy
        fields = ['name','company_name','salary','skills','duties','address']