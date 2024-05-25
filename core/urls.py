from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path("", views.ProductList.as_view(), name="product_list"),
    path(
        "category/<slug:category>/",
        views.ProductList.as_view(),
        name="product_category_list",
    ),
    path(
        "gender/<str:gender>/",
        views.ProductList.as_view(),
        name="product_gender_list",
    ),
    path(
        "size/<slug:size>/",
        views.ProductList.as_view(),
        name="product_size_list",
    ),
    path(
        "color/<slug:color>/",
        views.ProductList.as_view(),
        name="product_color_list",
    ),
    path("<int:id>/<slug:slug>/", views.ProductDetail.as_view(), name="product_detail"),
]
