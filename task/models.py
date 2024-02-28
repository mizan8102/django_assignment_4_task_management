from django.db import models
from category.models import CategoryModel

# Create your models here.
class TaskModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null = True)
    is_completed = models.BooleanField(default= False)
    assign_date = models.DateField()
    category = models.ManyToManyField(CategoryModel)

    def __str__(self) -> str:
        return self.name