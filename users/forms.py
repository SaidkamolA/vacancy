from django import forms

from users.models import User


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password','email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

