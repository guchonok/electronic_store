from django import template
from django.core.paginator import Paginator

from mainapp.models import *

register = template.Library()


@register.inclusion_tag('mainapp/template_tags/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}


@register.inclusion_tag('mainapp/template_tags/list_tags.html')
def show_tags(sort=None, tag_selected=0):
    if not sort:
        tags = Tags.objects.all()
    else:
        tags = Tags.objects.order_by(sort)

    return {"tags": tags, "tag_selected": tag_selected}


