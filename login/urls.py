from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login.as_view(), name='login'),
    path('getcookie/', views.getcookie, name='getcookie'),
    path('logout/', views.logout, name='logout'),
    path('main_page/', views.main_page, name='main_page'),
]