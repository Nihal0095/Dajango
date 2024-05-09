from django.urls import path
from . import views

urlpatterns = [
    path("show/", views.display, name='display'),
    path("showhello/", views.teamDetails, name='teamDetails'),
    path("myplayer/", views.myplayer_list, name='myplayer_list')
]
