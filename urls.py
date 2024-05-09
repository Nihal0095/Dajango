from django.urls import path
from . import views
from django.conf.urls.static import static 

urlpatterns =[
    path('',views.list_page,name='list'),
    path('login/',views.user_login,name='login'),
    path('signup/',views.user_signup,name='signup'),
    path('logout/',views.user_logout,name='logout'),
    path('<int:id>',views.user ,name='details'),
    path('home/',views.home,name='home'),
    path('product',views.product,name='product'),
    path('rangelist/',views.student_range_list_view),
    path('hello',views.hello,name='hello'),
    path('search',views.search,name='search'),
    path('productlist/',views.product_list,name='product_list'),
    path('cart/',views.view_cart,name='view_cart'),
    path('add/<int:product_id>',views.add_to_cart,name='add_to_cart'),
    path('remove/<int:item_id>',views.remove_from_cart,name='remove_from_cart'),
                       ]