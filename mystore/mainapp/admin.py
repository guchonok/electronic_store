from django.contrib import admin
from .models import *


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'cost', 'photo', 'is_published', 'author')
    list_display_links = ('id', 'title', 'category')
    search_fields = ('title', 'cost',)
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'surname',)
    list_display_links = ('user',)
    search_fields = ('user',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Profile, ProfileAdmin)
