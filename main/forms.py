from django import forms


class SearchForm(forms.Form):
    """Форма поиска по наименованию рецепта"""
    recipe_title = forms.CharField(label="Поиск по наименованию рецепта",required=False)

