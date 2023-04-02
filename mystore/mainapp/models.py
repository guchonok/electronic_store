from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django.template.defaultfilters import slugify

User = get_user_model()


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
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name='URL', blank=True, unique=True)
    avatar = models.ImageField(verbose_name='Аватар', default='default_pic.jpg', upload_to='avatar/')
    name = models.CharField(verbose_name='Имя', max_length=20, blank=True)
    surname = models.CharField(verbose_name='Фамилия', max_length=20, blank=True)
    phone = models.CharField(verbose_name='Телефон', max_length=10, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ('user',)
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def save(self, *args, **kwargs):
        """
        Сохранение полей модели при их отсутствии заполнения
        """
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'profile_slug': self.slug})
