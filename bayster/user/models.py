from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def _create_user(self, email, username, is_manager, password, **extra_fields):
        user = self.model(email=email, username=username, is_manager=is_manager, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, username, is_manager, password, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email=email, username=username, is_manager=is_manager, password=password,
                                 **extra_fields)

    def create_superuser(self, email, username, is_manager, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email=email, username=username, is_manager=is_manager, password=password,
                                 **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150)
    is_manager = models.BooleanField(default=False)

    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username", "is_manager",)
    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = verbose_name_plural = "ユーザ"
