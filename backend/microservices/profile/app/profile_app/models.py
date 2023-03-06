from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str):
        if not email:
            raise ValueError("Email Обязательное Поле!")
        elif not password:
            raise ValueError("password Обязательное Поле!")

        user = self.model(email=email)
        user.set_password(password)
        user.is_superuser = False
        user.is_admin = False
        user.is_staff = False
        user.is_active = False
        user.save(using=self._db)

        return user

    def create_superuser(self, email: str, password: str):
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)

        return user


class User(AbstractUser):
    first_name = None
    last_name = None

    surname = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Фамилия",
    )
    patronymic = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Отчество",
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Возраст",
    )
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
        verbose_name="Email",
    )
    phone = models.CharField(
        max_length=18,
        null=True,
        blank=True,
        verbose_name="Телефон",
    )
    rating = models.FloatField(
        default=0,
        null=False,
        blank=False,
        verbose_name="Рейтинг",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"

    def __str__(self) -> str:
        return f"Профиль {self.email}"
