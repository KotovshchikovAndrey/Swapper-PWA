from django.db import models


class UserProfile(models.Model):
    username = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Имя",
    )
    surname = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Фамилия",
    )
    patronymic = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Отчество",
    )
    age = models.PositiveIntegerField(
        null=False,
        blank=False,
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

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"

    def __str__(self) -> str:
        return f"{self.surname} {self.username}"


class Swap(models.Model):
    user_profile = models.ForeignKey(
        "UserProfile",
        on_delete=models.CASCADE,
        related_name="swaps",
        verbose_name="Пользователь",
    )
    date = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
        verbose_name="Дата совершения обмена",
    )
    description = models.TextField(
        null=False,
        blank=False,
        verbose_name="Описание/Условия обмена",
    )
    assessment = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Оценка обмена",
    )
    is_active = models.BooleanField(
        default=True,
        null=False,
        blank=False,
        verbose_name="Активность сделки",
    )
    is_end = models.BooleanField(
        default=False,
        null=False,
        blank=False,
        verbose_name="Окончание сделки",
    )

    class Meta:
        verbose_name = "Обмен"
        verbose_name_plural = "Обмены"

    def __str__(self) -> str:
        return f"Обмен с пользователем {self.user_profile}"


class SwapHistory(models.Model):
    user_profile = models.OneToOneField(
        "UserProfile",
        on_delete=models.CASCADE,
        related_name="swap_history",
        verbose_name="Пользователь",
    )
    swaps = models.ManyToManyField("Swap", verbose_name="Обмены")

    class Meta:
        verbose_name_plural = "История обменов"

    def __str__(self) -> str:
        return f"История обменов пользователя {self.user_profile}"
