from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Категория')
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class Tags(models.Model):
    name = models.CharField(max_length=100, verbose_name='Тэг')
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})

class Products(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    short_description = models.CharField(max_length=150, verbose_name='Краткое описание')
    cost = models.IntegerField(verbose_name='Цена')
    photo = models.ImageField(upload_to="prodacts/%Y/%m/%d/", verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name='URL')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT, null=True)
    tags = models.ManyToManyField(Tags, verbose_name='Тэги')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
