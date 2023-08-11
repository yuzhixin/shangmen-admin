from django.urls import path
from shangmen import views

urlpatterns = [
    path('home_info/', views.home_info, name='home_info'),
    path('shop_info/', views.shop_info, name='shop_info'),
    path('shangpin_list/', views.shangpin_list, name='shangpin_list'),
    path('code_to_session/', views.code_to_session, name='code_to_session'),
    path('login/', views.login, name='login'),
    path('current_user/', views.current_user, name='current_user'),
    path('update_current_user/', views.update_current_user,
         name='update_current_user'),
    path('address_list/', views.address_list, name='address_list'),
    path('default_address/', views.default_address, name='default_address'),
    path('set_default_address/', views.set_default_address,
         name='set_default_address'),
    path('add_address/', views.add_address, name='add_address'),
    path('update_address/', views.update_address, name='update_address'),
    path('create_order/', views.create_order, name='create_order'),
    path('order_list/', views.order_list, name='order_list'),
]
