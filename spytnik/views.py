from django.shortcuts import render
from django.views.generic import ListView

from spytnik.models import Post


class PostListView(ListView):
    model = Post

# Create your views here.
class HomeView(ListView):
    model = Post
    paginate_by = 12
    template_name = "spytnik/index.html"

