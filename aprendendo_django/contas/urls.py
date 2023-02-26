from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'$^',views.pagina_inicial),
    url(r'^login/',views.login),
    url(r'^registro/',views.registro)

]