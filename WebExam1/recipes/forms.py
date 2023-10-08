from django import forms

from WebExam1.recipes.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"


# class RecipeDeleteForm(ModelForm):
#     class Meta:
#         model = Recipe
#         fields = '__all__'
#
#     def save(self, commit=True):
#         if commit:
#             self.instance.delete()
#         return self.instance
