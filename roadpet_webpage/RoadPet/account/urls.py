from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/index.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('mypage/inquiry/', views.inquiry, name='inquiry'),
    path('mypage/survey_info/', views.survey_info, name='survey_info'),
    path('mypage/user_info/', views.user_info, name='user_info'),
    path('mypage/', views.mypage, name='mypage'),
    
]
