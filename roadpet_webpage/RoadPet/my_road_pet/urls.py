from django.urls import path,  include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/', views.about_us, name='about_us'),
    path('recommend/presurvey/survey/', views.survey, name='survey'),
    path('recommend/presurvey/', views.presurvey, name='presurvey'),
    path('recommend/', views.recommend, name='recommend'),
    path('search/', views.search, name='search'),
    path('search/filter/', views.search_filter, name='search_filter'),
    path('detail_info/adop_inquiry/', views.adoption_inquiry, name='adop_inquiry'),
    path('detail_info/<str:desertion_num>/', views.detail_info, name='detail'),
    path('detail_info/savestar/<str:desertion_num>/', views.savestar, name='savestar'),
]
