from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/', views.about_us, name='about_us'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/mypage/inquiry/', views.inquiry, name='inquiry'),
    path('accounts/mypage/survey_info/', views.survey_info, name='survey_info'),
    path('accounts/mypage/user_info/', views.user_info, name='user_info'),
    path('accounts/mypage/', views.mypage, name='mypage'),
    path('recommend/presurvey/survey/', views.survey, name='survey'),
    path('recommend/presurvey/', views.presurvey, name='presurvey'),
    path('recommend/', views.recommend, name='recommend'),
    path('search/', views.search, name='search'),
    path('detail_info/', views.detail_info, name='detail'),
]