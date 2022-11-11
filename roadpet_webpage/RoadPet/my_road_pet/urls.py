from django.urls import path,  include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/', views.about_us, name='about_us'),
    path('recommend/presurvey/survey/', views.survey, name='survey'),
    path('recommend/presurvey/', views.presurvey, name='presurvey'),
    path('recommend/', views.recommend, name='recommend'),
    path('search/', views.search, name='search'),
    path('detail_info/<str:desertion_num>/', views.detail_info, name='detail'),
]
