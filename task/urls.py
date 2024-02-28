from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.save, name='add_task'),
    path('edit/<int:id>', views.edit, name='edit_task'),
    path('delete/<int:id>', views.delete, name='delete_task')
]
