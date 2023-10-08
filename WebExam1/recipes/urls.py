from django.urls import path

from WebExam1.recipes.views import home_page, create, edit, delete, details

urlpatterns = (
    path('', home_page, name='index'),
    path('create/', create, name='create'),
    path('edit/<int:id>/', edit, name='edit'),
    path('delete/<int:id>/', delete, name='delete'),
    path('details/<int:id>/', details, name='details'),
)