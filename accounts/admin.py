from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm
)
from .models import CustomUser


class CustomUserAdmim(UserAdmin):
    model = CustomUser
    list_display = [
        "username", "email", "last_name", "first_name",
        "role", "team", "is_staff"
    ]
    add_form =  CustomUserCreationForm
    form = CustomUserChangeForm
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("None", {"fields": ("role", "team")}),
    )
    fieldsets = UserAdmin.fieldsets + (
        ("None", {"fields": ("role", "team")}),
    )

admin.site.register(CustomUser, CustomUserAdmim)