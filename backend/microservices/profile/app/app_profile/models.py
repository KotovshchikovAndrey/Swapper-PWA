from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name="Имя")
    surname = models.CharField(max_length=100, null=False, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=100, null=True, verbose_name="Отчество")
    email = models.EmailField(unique=True, null=False, verbose_name="Email")
    age = models.IntegerField(null=False, verbose_name="Возраст")
    phone = models.CharField(max_length=18, null=True, verbose_name="Телефон")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return f"{self.surname} {self.name}"


class Swap(models.Model):
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата совершения обмена"
    )
    description = models.TextField(null=False, verbose_name="Описание/Условия обмена")

    class Meta:
        verbose_name = "Обмен"
        verbose_name_plural = "Обмены"

    def __str__(self) -> str:
        return f"Обмен с пользователем {self.user}"


class SwapHistory(models.Model):
    user = models.OneToOneField(
        "User", on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    swaps = models.ManyToManyField("Swap", verbose_name="Обмены")

    class Meta:
        verbose_name_plural = "История обменов"

    def __str__(self) -> str:
        return f"История обменов пользователя {self.user}"
