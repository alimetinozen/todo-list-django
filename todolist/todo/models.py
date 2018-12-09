from django.db import models
from django.utils import timezone


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Todo(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=40, blank=False)
    created_at = models.DateField(default=timezone.now().strftime('%Y-%m-%d'))
    due_date = models.DateField(default=timezone.now().strftime('%Y-%m-%d'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
