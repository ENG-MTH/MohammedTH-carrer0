from django.urls import path

from . import views

urlpatterns = {
    path('as', views.index, name='index'),
    path('new', views.newPost, name='new'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')

}