from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import Products, Category, Tags

main_menu = [
    {'title': 'Гарантия', 'url_name': 'guarantee'},
    {'title': 'Оплата', 'url_name': 'payment'},
    {'title': 'О нас', 'url_name': 'about_us'},
    {'title': 'Контакты', 'url_name': 'contacts'},
]
head_menu = [
    {'title': 'Тэги', 'url_name': 'tags'},
    {'title': 'Купить', 'url_name': 'buy'},
    {'title': 'Продать товар', 'url_name': 'sell'},
]


# def main_page(request):
#     category = Category.objects.all()
#     tags = Tags.objects.all()
#     context = {
#         'category': category,
#         'tags': tags,
#         'menu': main_menu,
#     }
#     return render(request, 'mainapp/main_page.html', context=context)


def index(request):
    category = Category.objects.all()
    tags = Tags.objects.all()

    context = {
        'category': category,
        'tags': tags,
        'menu': main_menu,
        'cat_selected': 0,
    }
    return render(request, 'mainapp/home.html', context=context)


def show_post(request, post_slug):
    tags = Tags.objects.all()
    category = Category.objects.all()
    products = Products.objects.filter(slug=post_slug)
    context = {
        'category': category,
        'tags': tags,
        'products': products,
        'menu': main_menu,
        'cat_selected': 0,
    }
    return render(request, 'mainapp/show_post.html', context=context)


def show_category(request, cat_slug):
    tags = Tags.objects.all()
    category = Category.objects.all()
    products = Products.objects.filter(category__slug=cat_slug)
    context = {
        'category': category,
        'tags': tags,
        'products': products,
        'menu': main_menu,
        'cat_selected': cat_slug,
    }
    return render(request, 'mainapp/list_posts.html', context=context)


def show_tag(request, tag_slug):
    tags = Tags.objects.all()
    category = Category.objects.all()
    products = Products.objects.filter(tags__slug=tag_slug)
    context = {
        'category': category,
        'tags': tags,
        'products': products,
        'menu': main_menu,
    }
    return render(request, 'mainapp/list_posts.html', context=context)


def about_us(request):
    return render(request, 'mainapp/about_us.html', {'menu': main_menu})


def contacts(request):
    return render(request, 'mainapp/contacts.html', {'menu': main_menu})


def guarantee(request):
    return render(request, 'mainapp/guarantee.html', {'menu': main_menu})


def payment(request):
    return render(request, 'mainapp/payment.html', {'menu': main_menu})

    # return HttpResponse(f'Отображение новости id = {post_id}')
    # category = Category.objects.all()
    # products = Products.objects.filter(cat_id=cat_id)
    # context = {
    #     'category': category,
    #     'products': products,
    #     'menu': menu,
    #     'cat_selected': cat_id,
    # }
    # return render(request, 'mainapp/show_post.html', context=context)
    # products = Products.objects.all()
    # return render(request, 'mainapp/list_posts.html', {'products': products})

# class ProductCategory(ListView):
#     model = Category

# class ProductHome(ListView):
#     model = Products
