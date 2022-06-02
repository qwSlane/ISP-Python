import json
from datetime import datetime
from pprint import pprint

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from spytnik.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . models import Pleb, Vote, Genre


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(genre__slug=self.kwargs.get("slug"))


    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)

        slug = self.request.path
        slug = slug[1:]

        tags = Genre.objects.all()
        for tag in tags:
            if tag.slug == slug:
                context['tag'] = tag.name
                t = tag
        return context


class InfoView(ListView):
    template_name = 'spytnik/info.html'

    def get_queryset(self):
        return Post.objects.filter(isChosen=True).select_related()


class ProfileView(ListView):
    model = Vote
    template_name = 'spytnik/account.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Vote.objects.filter(user=self.request.user).select_related()

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)

        votes = Vote.objects.filter(user=self.request.user).select_related()
        count = votes.count()
        sum = 0
        for vot in votes:
            sum += vot.value
        if count > 0:
            context['average'] = sum/count
        else:
            context['average'] = "--"
        return context

    def post(self, request, *args, **kwargs):
        print(request.POST.get("submit"))
        if request.POST.get("submit"):
            logout(request)
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)


class TitleView(DetailView):
    model = Post
    slug_url_kwarg = 'title_slug'
    context_object_name = "post"
    template_name = "spytnik/title.html"

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        item = kwargs.get('object')
        votes = Vote.objects.filter(post__slug=item.slug).select_related()
        if votes.count() > 0:
            sum = 0
            for vot in votes:
                sum += vot.value
            context['average'] = sum/votes.count()
        else:
            context['average'] = '--'
        return context

    def post(self, request, *args, **kwargs):
        value = 0
        if request.POST.get('submit') == 's_1':
            value = 1
        elif request.POST.get('submit') == 's_2':
            value = 2
        elif request.POST.get('submit') == 's_3':
            value = 3
        elif request.POST.get('submit') == 's_4':
            value = 4
        elif request.POST.get('submit') == 's_5':
            value = 5

        current = Post.objects.filter(slug=self.kwargs['title_slug']).select_related().first()
        t = Vote.objects.all().filter(user=self.request.user, post=current)
        print(t)
        if t.count() > 0:
            temp = t.first()
            print(temp.voted_date)
            temp.value = value
            temp.voted_date = datetime.now()
            temp.save()
        else:
            vote = Vote(value=value, user=self.request.user, post=current, voted_date=datetime.now())
            vote.save()
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


class HomeView(ListView):
    model = Post
    paginate_by = 12
    template_name = "spytnik/index.html"

    def post(self, request):
        print(request.POST)
        if request.POST.get("reg_username") is None:
            name = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=name, password=password)
            if user:
                login(request, user)
                return JsonResponse(data={'url': 'user/' + name}, status=201)
            return JsonResponse(data={'error': "Неверное емя пользователя или пароль"}, status=400)
        else:
            name = request.POST.get("reg_username")
            pass1 = request.POST.get("reg_pass1")
            user = User.objects.create_user(username=name, password=pass1)
            print(user)
            if user:
                user.save()
                plebs = Pleb(user=user)
                plebs.save()
                login(request, user)
                return JsonResponse(data={'url': 'user/' + name}, status=201)
            return JsonResponse(data={'error': "Данное имя пользователя уже используется"}, status=400)



