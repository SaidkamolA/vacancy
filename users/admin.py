from django.contrib import admin

from users.models import Role, User

# Register your models here.
admin.site.register(Role)
admin.site.register(User)

