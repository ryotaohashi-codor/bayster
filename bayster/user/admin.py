from django.contrib import admin
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "is_manager", "is_superuser")
    fields = ("email", "username", "is_manager", "is_superuser")