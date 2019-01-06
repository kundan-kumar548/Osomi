from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from accounts import urls
from home import urls
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^api/accounts/', include('accounts.urls')),
    url('^api/home/', include('home.urls',namespace="home")),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()