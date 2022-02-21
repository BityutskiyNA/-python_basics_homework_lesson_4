from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField("Время создания записи", auto_now_add=True)
    updated_at = models.DateTimeField("Время обновления записи", auto_now=True)

    class Meta:
        abstract = True


class Ingredient(TimeStampMixin):
    """" Модель ингридиента"""
    name = models.CharField("Наименование", max_length=50, null=False)

    def __str__(self):
        return f"{self.name}".strip()

    class Meta:
        app_label = "main"
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"


class Recipe(TimeStampMixin):
    """" Модель рецепта"""
    ingredients = models.ManyToManyField("Ingredient", verbose_name="Ингредиент", related_name="ingredient_ob",)
    title = models.CharField(verbose_name="Название", max_length=255, null=False, blank=False, db_index=True)
    recipe = models.TextField(verbose_name="Описание")


    def __str__(self):
        return f"{self.title}"

    class Meta:
        app_label = "main"
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"