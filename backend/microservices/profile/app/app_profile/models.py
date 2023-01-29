from django.db import models


class User(models.Model):
    name = models.CharField(
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
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return f"{self.surname} {self.name}"


class Swap(models.Model):
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
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

    class Meta:
        verbose_name = "Обмен"
        verbose_name_plural = "Обмены"

    def __str__(self) -> str:
        return f"Обмен с пользователем {self.user}"


class SwapHistory(models.Model):
    user = models.OneToOneField(
        "User",
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )
    swaps = models.ManyToManyField("Swap", verbose_name="Обмены")

    class Meta:
        verbose_name_plural = "История обменов"

    def __str__(self) -> str:
        return f"История обменов пользователя {self.user}"
