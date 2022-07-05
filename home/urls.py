from django.urls import path
from .views import ItemListView, ItemDetailView, ItemCreateView

urlpatterns = [
    path("", ItemListView.as_view(), name="home"),
    path("items/<int:pk>/", ItemDetailView.as_view(), name="item_detail"),
    path("items/new/", ItemCreateView.as_view(), name="item_new"),
]
