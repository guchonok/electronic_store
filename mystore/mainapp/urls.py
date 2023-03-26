from django.conf.urls.static import static
from django.urls import path

from mystore import settings
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about_us/', about_us, name='about_us'),
    path('contacts/', contacts, name='contacts'),
    path('payment/', payment, name='payment'),
    path('guarantee/', guarantee, name='guarantee'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:cat_slug>/', show_category, name='category'),
    path('tag/<slug:tag_slug>/', show_tag, name='tag'),
]
