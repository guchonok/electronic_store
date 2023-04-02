from django.db.models import Count
from django.core.cache import cache

from mainapp.models import *

main_menu = [
    {'title': 'Гарантия', 'url_name': 'guarantee'},
    {'title': 'Оплата', 'url_name': 'payment'},
    {'title': 'О нас', 'url_name': 'about_us'},
    {'title': 'Контакты', 'url_name': 'contacts'},
]


