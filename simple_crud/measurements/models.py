from django.db import models


class Project(models.Model):
    """Объект, на котором проводят измерения."""

    name = models.TextField(verbose_name="Название объекта")
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )

    def __str__(self):
        return f"{self.id}: {self.name}"

    class Meta:
        verbose_name = "Объект, на котором проводят измерения"
        verbose_name_plural = "Объекты, на котором проводят измерения"


class Measurement(models.Model):
    """Измерение температуры на объекте."""

    value = models.FloatField(verbose_name="Температура при измерении")
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        verbose_name="Объект, на котором проводят измерения")
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )

    def __str__(self):
        return f"{self.id} - температура при измерении: {self.value}, " \
               f"дата создания: {self.created_at}, дата обновления: {self.updated_at}"

    class Meta:
        verbose_name = "Температура"
        verbose_name_plural = "Данные температуры"
