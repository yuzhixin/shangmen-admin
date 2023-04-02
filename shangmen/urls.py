from django.urls import path
from shangmen import views

urlpatterns = [
    path('home_info/', views.home_info, name='home_info'),
    path('shop_info/', views.shop_info, name='shop_info'),
    path('shangpin_list/', views.shangpin_list, name='shangpin_list'),
    path('code_to_session/', views.code_to_session, name='code_to_session'),
    path('get_current_user/', views.get_current_user, name='get_current_user'),
    path('update_current_user/', views.update_current_user,
         name='update_current_user'),
]
