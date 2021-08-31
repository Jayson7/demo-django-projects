
from django.contrib import admin
from django.urls import path
from mini import views 
from mini.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('add', views.add, name="add"),
    path('delete/<int:pk>' , views.delete, name="delete"),
    path('update/<int:pk>' , views.edit, name="update"),



    

]