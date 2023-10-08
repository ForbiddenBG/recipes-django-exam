from django.contrib import admin

from WebExam1.recipes.models import Recipe


# Register your models here.
@admin.register(Recipe)
class AdminRecipe(admin.ModelAdmin):
    list_display = ("title", )
