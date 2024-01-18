from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('index', views.index, name='index'),
    path('katha', views.katha, name='katha'),
    path('shokseva', views.shokseva, name='shokseva'),
    path('birthday', views.birthday, name='birthday'),
    path('wedding', views.wedding, name='wedding'),
    path('team', views.team, name='team'),
    path('signup_login', views.signup_login, name='signup_login'),
    path('submit/', views.submit_form, name='submit_form'),

]