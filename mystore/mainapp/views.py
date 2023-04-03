from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .models import Products, Category, Tags, Profile
from .forms import RegistrationForm, LoginUserForm, UpdateProfileForm, SellProduct

main_menu = [
    {'title': 'Гарантия', 'url_name': 'guarantee'},
    {'title': 'Оплата', 'url_name': 'payment'},
    {'title': 'О нас', 'url_name': 'about_us'},
    {'title': 'Контакты', 'url_name': 'contacts'},
]


def index(request):
    context = {
        'menu': main_menu,
        'cat_selected': 0,
    }
    return render(request, 'mainapp/home.html', context=context)


def show_post(request, post_slug):
    products = Products.objects.filter(slug=post_slug)

    context = {
        'products': products,
        'menu': main_menu,
        'cat_selected': post_slug,

    }
    return render(request, 'mainapp/show_post.html', context=context)


def show_category(request, cat_slug):
    products = Products.objects.filter(category__slug=cat_slug)

    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {
        'menu': main_menu,
        'cat_selected': cat_slug,
        'page_obj': page_obj,
    }
    return render(request, 'mainapp/list_posts.html', context=context)


def show_tag(request, tag_slug):
    products = Products.objects.filter(tags__slug=tag_slug)

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'menu': main_menu,
        'tag_selected': tag_slug,
        'page_obj': page_obj,
    }
    return render(request, 'mainapp/list_posts.html', context=context)


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            print(user.username)
            return HttpResponseRedirect('/login/')
    else:
        form = RegistrationForm()
    return render(request, 'mainapp/registration.html', {'form': form, 'menu': main_menu})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(user.check_password('09q08a07zQ'))
            return HttpResponseRedirect('/profile/' + username)
    else:
        redirect('home')
    return render(request, 'mainapp/login.html', {'menu': main_menu})


@login_required
def user_profile(request, profile_slug):
    user = User.objects.get(username=profile_slug)
    profile = Profile.objects.get(user=user)
    context = {
        'user': user,
        'profile': profile,
        'menu': main_menu,
    }
    return render(request, 'mainapp/user_page.html', context=context)


def update_profile(request, profile_slug):
    user = User.objects.get(username=profile_slug)
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return HttpResponseRedirect('/profile/' + profile.slug)
    else:
        profile_form = UpdateProfileForm()
    context = {
        'profile': profile,
        'menu': main_menu,
        'profile_form': profile_form,
    }
    return render(request, 'mainapp/update_profile.html', context=context)


def sell_product(request, profile_slug):
    user = User.objects.get(username=profile_slug)
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
        product = SellProduct(request.POST, request.FILES)
        if product.is_valid():
            obj_author = product.save(commit=False)
            obj_author.author = profile
            obj_author.save()
            product = SellProduct()
            return redirect('home')
    else:
        product = SellProduct()
    return render(request, 'mainapp/sell_product.html', {'product': product, 'menu': main_menu})


def user_post_product(request, profile_slug):
    user = User.objects.get(username=profile_slug)
    profile = Profile.objects.get(user=user)
    products = Products.objects.filter(author=profile)

    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {
        'menu': main_menu,
        'profile': profile,
        'page_obj': page_obj,
    }
    return render(request, 'mainapp/list_posts.html', context=context)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


def about_us(request):
    return render(request, 'mainapp/about_us.html', {'menu': main_menu})


def contacts(request):
    return render(request, 'mainapp/contacts.html', {'menu': main_menu})


def guarantee(request):
    return render(request, 'mainapp/guarantee.html', {'menu': main_menu})


def payment(request):
    return render(request, 'mainapp/payment.html', {'menu': main_menu})
