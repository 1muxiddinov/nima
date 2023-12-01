from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['surname','number','message','yoshi',]
    search_fields = ['surname']
