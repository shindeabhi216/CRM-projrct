from django.urls import path
from accounts import views
urlpatterns = [
    path('home/',views.home,name='home'),
    path('',views.home,name='home'),
    path('product',views.product,name='product'),
    path('customer/<str_pk>',views.customer,name='customer'),
    path('update_order/<pk>',views.update_order,name='update_order'),
   # path('create_order/',views.create_order,name='create_order'),
    path('create_order/',views.create_order,name='create_order'),
    path('delete_order/<pk>',views.delete_order,name='delete_order'),
    path('update_customer/<pk>',views.update_customer,name='update_customer'),
    path('delete_customer/<pk>',views.delete_customer,name='delete_customer'),
    path('update_product/<pk>',views.update_product,name='update_product',),
    path('delete_product/<pk>',views.delete_product,name='delete_product',),

    path('register/',views.registerpage,name='register'),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutpage,name='logout'),
    path('user/',views.userPage,name='user-page')

]
