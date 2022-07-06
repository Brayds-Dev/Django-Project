from django.urls import path
from .views import ItemListView, ItemDetailView, ItemCreateView, ItemDeleteView, ItemUpdateView

urlpatterns = [
    path("items/new/", ItemCreateView.as_view(), name="item_new"),
    path("items/<int:pk>/", ItemDetailView.as_view(), name="item_detail"),
    path("items/<int:pk>/edit/", ItemUpdateView.as_view(), name="item_edit"),
    path("items/<int:pk>/delete/", ItemDeleteView.as_view(), name="item_delete"),
    path("", ItemListView.as_view(), name="home"),
    
    
]
