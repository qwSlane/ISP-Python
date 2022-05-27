from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('<slug:slug>/', views.PostListView.as_view(), name="posts"),
    path('<slug:slug>/<slug:title_slug>', views.TitleView.as_view(), name="title")

]