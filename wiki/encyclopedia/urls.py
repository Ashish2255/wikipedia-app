from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("display/<str:entry>", views.display, name="display"),
    path("edit",views.edit,name="edit"),
    path("search",views.search,name="search"),
    path("create_new",views.create_file,name="create_new"),
    path("new",views.new,name="new"),
    path("<str:name>",views.title,name="title"),
]
