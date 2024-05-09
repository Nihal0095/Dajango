from django.urls import path
from . import views
urlpatterns = [path('home/',views.home,name='home'),
               path('',views.shoes,name='shoes'),
               path('mens/',views.mens,name='mens'),
               path('<int:id>',views.detail_page,name='detail'),
               ]