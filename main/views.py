from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.db.models import Q
from main.models import Ingredient, Recipe
from main.forms import SearchForm

def index (request):
    try:
        recipe_id = int(request.GET.get("recipe_id"))
    except (ValueError, TypeError):
        recipe_id = None
    try:
        recipe_ingredient_id = int(request.GET.get("ingredient_id"))
    except (ValueError, TypeError):
        recipe_ingredient_id = None

    query = Q()
    if recipe_id:
        query.add(Q(pk=recipe_id), Q.AND,)
    if recipe_ingredient_id:
        query.add(Q(ingredients__pk=recipe_ingredient_id), Q.AND,)
    if 'recipe_title' in request.GET:
        keyword = request.GET['recipe_title']
        if keyword != "":
            q = Q(title__icontains=keyword)
            recipe_objects = Recipe.objects.filter(q)
        else:
            recipe_objects = Recipe.objects.prefetch_related("ingredients").filter(query)
    else:
        recipe_objects = Recipe.objects.prefetch_related("ingredients").filter(query)

    ingredient_lookup = Ingredient.objects.all()
    recipe_lookup = Recipe.objects.all()
    recipe_title_form = SearchForm()
    return render(
        request,
        "main/index.html",
        {
            "recipes": recipe_objects,
            "form": {
                "description": "Список рецептов",
                "ingredient": {
                    "title": "Поиск по ингредиенту",
                    "objects": ingredient_lookup,
                    "selected": recipe_ingredient_id,
                },
                "recipe": {
                    "title": "Поиск по рецепту",
                    "objects": recipe_lookup,
                    "selected": recipe_id,
                },
                "recipe_title_form": recipe_title_form

            },
        },
    )