from django.urls import path
from .import views

urlpatterns = [
    path('',views.base,name='base'),
    path('user_login/',views.user_login,name='login'),
    path('user_signup/',views.user_signup,name='signup'),
    path('user_logout',views.user_logout,name='logout')
]
