from django.conf.urls import url
from . import views
from django.urls import path,include
from django.contrib.auth import views as auth_views
# app_name = 'accounts'
from rest_framework import routers
router = routers.DefaultRouter()
router.register('auth-user',views.UserDetailView)
router.register('user',views.UserListView,base_name='users')
router.register('address',views.AddressView,base_name='address')
router.register('profile',views.UserProfileView,base_name='usersprofile')
router.register('artist',views.ArtistAccountView,base_name='artistaccount')

urlpatterns = [
        path('', include(router.urls)),
        url(r'signup', views.UserSignupView.as_view(), name='signup'),
        url(r'login', views.LoginLoginView.as_view(), name='login'),
]