from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm
from .models import Item
# Create your views here.

class ItemListView(ListView):
    model = Item
    template_name = "home/home.html"

class ItemDetailView(DetailView):
    model = Item
    template_name = "home/item_detail.html"

    #Comment context data here for adding comments
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

    success_url = reverse_lazy("home")

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

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