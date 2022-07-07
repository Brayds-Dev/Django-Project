from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Item
# Create your views here.

class AboutView(TemplateView):
    template_name = "home/about.html"

class ItemListView(ListView):
    model = Item
    template_name = "home/home.html"

class ItemDetailView(DetailView):
    model = Item
    template_name = "home/item_detail.html"

    # Will be adding comment context data here for adding comments

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = "home/item_new.html"
    fields = ["title", "description", "price", "condition"]
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    template_name = "home/item_edit.html"
    fields = ["title", "description", "price", "condition"]
    

    def test_func(self):  # new
        obj = self.get_object()
        return obj.user == self.request.user

class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = "home/item_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):  # new
        obj = self.get_object()
        return obj.user == self.request.user