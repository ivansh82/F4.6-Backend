from django.contrib import admin
from .models import Category, Recipe, RecipeCategory


class RecipeCategoryInline(admin.TabularInline):
    model = RecipeCategory
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeCategoryInline,)
    list_display = ['pk', 'title', 'author', 'in_category', 'date_posted']
    list_display_links = ('pk', 'title',)
    list_filter = ('title', 'author', 'category', 'date_posted')  # добавляем примитивные фильтры в нашу админку
    search_fields = ('title', 'author__username', 'category__name')  # тут всё очень похоже на фильтры из запросов в базу


admin.site.register(Category)
admin.site.register(Recipe, RecipeAdmin)
