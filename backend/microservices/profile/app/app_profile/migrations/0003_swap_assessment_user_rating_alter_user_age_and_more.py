# Generated by Django 4.1.5 on 2023-01-29 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_profile", "0002_alter_swaphistory_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="swap",
            name="assessment",
            field=models.PositiveSmallIntegerField(
                blank=True, null=True, verbose_name="Оценка обмена"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="rating",
            field=models.FloatField(blank=True, default=0, verbose_name="Рейтинг"),
        ),
        migrations.AlterField(
            model_name="user",
            name="age",
            field=models.PositiveIntegerField(verbose_name="Возраст"),
        ),
        migrations.AlterField(
            model_name="user",
            name="patronymic",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Отчество"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.CharField(
                blank=True, max_length=18, null=True, verbose_name="Телефон"
            ),
        ),
    ]
