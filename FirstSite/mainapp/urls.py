from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path("new1/", views.new1, name="new1"),
    path("new2/", views.new2, name="new2"),
    path("new3/", views.new3, name="new3"),
    path("new4/", views.new4, name="new4"),
    path("new5/", views.new5, name="new5"),
    path("new6/", views.new6, name="new6"),
    path("new7/", views.new7, name="new7"),
    path("new8/", views.new8, name="new8"),
    path("new9/", views.new9, name="new9"),
    path("new10/", views.new10, name="new10"),
    path("new11/", views.new11, name="new11"),
    path("new12/", views.new12, name="new12"),
    path("new13/", views.new13, name="new13"),
    path("new14/", views.new14, name="new14"),
    path("new15/", views.new15, name="new15"),
    path("new16/", views.new16, name="new16"),
    path("new17/", views.new17, name="new17"),
    path("new18/", views.new18, name="new18"),
    path("new19/", views.new19, name="new19"),
    path("new20/", views.new20, name="new20"),
    path("new21/", views.new21, name="new21"),
    path("new22/", views.new22, name="new22"),
    path("new23/", views.new23, name="new23"),
    path("new24/", views.new24, name="new24"),
    path("new25/", views.new25, name="new25")
]