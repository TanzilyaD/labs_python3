from django.contrib import admin
from django.urls import path
from flatpages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('hello/', views.hello, name='hello'),
    path('hello-default/', views.hello_default, name='hello_default'),
    path('static-page/', views.static_page, name='static_page'),
]