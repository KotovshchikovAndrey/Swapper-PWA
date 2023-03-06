from django.db import models
from app import settings

from django.utils import timezone


class Swap(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="swaps",
        verbose_name="Пользователь",
    )
    date = models.DateTimeField(
        default=timezone.now,
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
        return f"Обмен с пользователем {self.user}"


class SwapHistory(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="swap_history",
        verbose_name="Пользователь",
    )
    swaps = models.ManyToManyField("Swap", verbose_name="Обмены", blank=True)

    class Meta:
        verbose_name_plural = "История обменов"

    def __str__(self) -> str:
        return f"История обменов пользователя {self.user.email}"
