from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('info/', views.InfoView.as_view(), name="info"),
    path('user/<username>', views.ProfileView.as_view(), name="profile"),
    path('offtop', views.PostListView.as_view(), name="other"),
    path('movies', views.PostListView.as_view(), name="movies"),
    path('music', views.PostListView.as_view(), name="music"),
    path('life', views.PostListView.as_view(), name="life"),
    path('<slug:slug>/', views.PostListView.as_view(), name="posts"),
    path('<slug:slug>/<slug:title_slug>', views.TitleView.as_view(), name="title"),


]
