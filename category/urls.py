from django.urls import path
from . import views

urlpatterns = [
    path('list_category', views.list_category, name='lsit_category'),
    path('add_category', views.add_category, name='add_category'),
    path('edit_category/<int:id>', views.edit_category, name='edit_category'),
    path('delete_category/<int:id>', views.delete_category, name='delete_category')
]
