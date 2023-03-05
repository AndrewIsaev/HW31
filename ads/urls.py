"""hw31 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework import routers

from ads import views
from django.urls import path
from django.conf.urls.static import static

from ads.views import AdViewSet
from hw31 import settings

ad_router = routers.SimpleRouter()
ad_router.register("ad", AdViewSet)

urlpatterns = [
    path('cat/', views.CategoryListView.as_view(), name="category_list"),
    path('cat/create/', views.CategoryCreateView.as_view(), name="category_create"),
    path('cat/<int:pk>/', views.CategoryDetailView.as_view(), name="category_detail"),
    path('cat/<int:pk>/update/', views.CategoryUpdateView.as_view(), name="category_update"),
    path('cat/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name="category_delete"),

    path("selection/", views.SelectionListView.as_view(), name="selection_list_view"),
    path("selection/<int:pk>/", views.SelectionDetailView.as_view(), name="selection_detail_view"),
    path("selection/<int:pk>/update/", views.SelectionUpdateView.as_view(), name="selection_update_view"),
    path("selection/<int:pk>/delete/", views.SelectionDeleteView.as_view(), name="selection_delete_view"),
    path("selection/create/", views.SelectionCreateView.as_view(), name="selection_create_view"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += ad_router.urls
