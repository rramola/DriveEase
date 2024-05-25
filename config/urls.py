"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from app.views import *
from django.views.static import serve

handler404 = "app.views.custom_404_view"

urlpatterns = [
    path("return-vehicle/<str:pk>/", return_vehicle_page, name="return-vehicle"),
    path("rent-vehicle/<str:pk>/", rent_vehicle_page, name="rent-vehicle"),
    path("new-listing/", new_listing_page, name="new-listing"),
    path("update-listing/<str:pk>/", update_listing, name="update-listing"),
    path("delete-listing/<str:pk>/", delete_listing, name="delete-listing"),
    path("garage/", garage_page, name="garage"),
    path("add-vehicle/", add_vehicle_page, name="add-vehicle"),
    path("update-vehicle/<str:pk>/", update_vehicle, name="update-vehicle"),
    path("delete-vehicle/<str:pk>/", delete_vehicle_page, name="delete-vehicle"),
    path("register/", registration_page, name="register"),
    path("login/", login_page, name="login"),
    path("logout/", logout_user, name="logout"),
    path("listings/", listings_page, name="listings"),
    path("", home_page, name="home"),
    path("admin/", admin.site.urls),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
