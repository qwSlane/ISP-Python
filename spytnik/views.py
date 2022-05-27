from pprint import pprint

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from spytnik.models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(genre__slug=self.kwargs.get("slug")).select_related()

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)

        slug = self.kwargs.get("slug")
        model = Post.objects.filter(genre__slug=slug).select_related().first()

        for tag in model.genre.all():
            if slug == tag.slug:
                context['tag'] = tag.name
        return context


class TitleView(DetailView):
    model = Post
    slug_url_kwarg = 'title_slug'
    context_object_name = "post"
    template_name = "spytnik/title.html"


class HomeView(ListView):
    model = Post
    paginate_by = 12
    template_name = "spytnik/index.html"

