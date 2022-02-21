from django.contrib import admin
from django.utils.safestring import mark_safe

# from booklist.filters import PublishingHouseFilter
from main.models import Ingredient, Recipe

# Register your models here.
@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):

    list_display = ('name', )
    search_fields = ('name', )
    ordering = ("name", )


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_display = ("title", "ingredient_list",)
    autocomplete_fields = ("ingredients",)

    ordering = ("title",)

    def ingredient_list(self, obj):
        if not obj.ingredients:
            return "-"

        return mark_safe("<br/>".join(str(ingredients) for ingredients in obj.ingredients.all()))

    ingredient_list.short_description = "Ингредиенты"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related("ingredients")

    class Media:
        pass