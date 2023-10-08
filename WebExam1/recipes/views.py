from django.shortcuts import render, redirect

from WebExam1.recipes.forms import RecipeForm
from WebExam1.recipes.models import Recipe


# Create your views here.
def home_page(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }

    return render(request, 'index.html', context)


def create(request):
    if request.method == "GET":
        form = RecipeForm()
    else:
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'create.html', {'form': form})

    context = {
        'form': form
    }

    return render(request, 'create.html', context)


def edit(request, id):
    recipe = Recipe.objects.filter(pk=id).get()
    ingredients = recipe.ingredients

    if request.method == "GET":
        form = RecipeForm(instance=recipe)
    else:
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'recipe': recipe,
        'ingredients': ingredients.split(", "),
    }

    return render(request, 'edit.html', context)


def delete(request, id):
    recipe = Recipe.objects.filter(pk=id).get()

    if request.method == "POST":
        recipe.delete()
        return redirect('index')

    context = {
        'recipe': recipe,
    }

    # recipe = Recipe.objects.filter(id=id).get()
    # form = RecipeDeleteForm(instance=recipe)
    # if request.method == "POST":
    #     form = RecipeDeleteForm(request.POST, instance=recipe)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('index')
    #
    # context = {
    #     'form': form,
    # }

    return render(request, 'delete.html', context)


def details(request, id):
    recipe = Recipe.objects.filter(pk=id).get()

    ingredients = recipe.ingredients

    context = {
        'recipe': recipe,
        'ingredients': ingredients.split(', '),
    }

    return render(request, 'details.html', context)
