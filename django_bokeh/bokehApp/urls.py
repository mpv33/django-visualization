from django.urls import path
from .import views

urlpatterns = [


    path("home", views.home, name="home"),
    path("starter/", views.starter, name="starter"),
    path("combo/", views.combo, name="combo"),
    path("programming/", views.programming, name="programming"),
    path("multi_plot/", views.multi_plot, name="multi_plot"),
    path("products/", views.products, name="products"),
    path("pie/", views.pie, name="pie"),



]
