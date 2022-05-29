import json
from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from spytnik.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate, login, logout
from . models import Pleb, Vote, Genre


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(genre__slug=self.kwargs.get("slug")).select_related()

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)

        slug = self.request.path
        slug = slug[1:]

        tags = Genre.objects.all()
        for tag in tags:
            if tag.slug == slug:
                context['tag'] = tag.name

        return context


class InfoView(ListView):
    template_name = 'spytnik/info.html'

    def get_queryset(self):
        return Post.objects.filter(genre__slug=self.kwargs.get("slug")).select_related()


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
        context['average'] = sum/count
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

    def post(self, request, *args, **kwargs):
        if request.POST.get('submit') == 'sign_in':

            name = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=name, password=password)
            if user is not None:
                login(request, user)
                return redirect('user/'+name)
            else:
                return redirect('')
        else:
            name = request.POST.get("reg_username")
            pass1 = request.POST.get("reg_pass1")
            pass2 = request.POST.get("reg_pass2")
            if pass1 == pass2:
                user = User.objects.create_user(name, password=pass1)
                user.save()
                plebs = Pleb(user=user)
                plebs.save()
                return redirect('/' + name)




