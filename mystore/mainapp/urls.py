from django.conf.urls.static import static
from django.urls import path, include

from mystore import settings
from .views import *

profile = [
    path('', user_profile, name='user_prof'),
    path('update/', update_profile, name='update_profile'),
    path('sell', sell_product, name='sell_product'),
    path('list_posts/', user_post_product, name='user_list_product'),
]

urlpatterns = [
    path('', index, name='home'),
    path('about_us/', about_us, name='about_us'),
    path('contacts/', contacts, name='contacts'),
    path('payment/', payment, name='payment'),
    path('guarantee/', guarantee, name='guarantee'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:cat_slug>/', show_category, name='category'),
    path('tag/<slug:tag_slug>/', show_tag, name='tag'),
    path('profile/<slug:profile_slug>/', include(profile)),
    path('registration/', registration, name='reg'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

]
