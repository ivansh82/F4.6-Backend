from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='img', max_length=254, blank=True)

    def __str__(self):
        return f'{self.name}'


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='RecipeCategory')
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    ingredients = models.TextField()
    cooking_method = models.TextField()
    photo1 = models.ImageField(upload_to='img', max_length=254, blank=True)
    photo2 = models.ImageField(upload_to='img', max_length=254, blank=True)
    photo3 = models.ImageField(upload_to='img', max_length=254, blank=True)
    rating = models.IntegerField(default=0)

    @property
    def in_category(self):
        list_of_category = [category.name for category in self.category.all()]
        return list_of_category

    def preview(self):
        return self.ingredients[:125] + '...'

    def get_absolute_url(self):  # добавим абсолютный путь чтобы после создания нас перебрасывало на страницу с новостью
        return f'/posts/{self.id}'

    def __str__(self):
        return f'{self.title}'


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
