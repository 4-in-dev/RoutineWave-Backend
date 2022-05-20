from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers


# from users.views import UserViewSet

# router = routers.DefaultRouter()
# router.register('user', UserViewSet)

urlpatterns = [
    # path("", TemplateView.as_view(template_name="index.html")),
    # path('users/', include('users.urls')),
    path('', include('dj_rest_auth.urls')),
    path('', include('dj_rest_auth.registration.urls')),
    path('', include('allauth.urls')),
    # path('', include(router.urls)),
]
