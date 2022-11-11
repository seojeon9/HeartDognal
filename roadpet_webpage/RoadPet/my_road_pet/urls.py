from django.urls import path,  include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/', views.about_us, name='about_us'),
    path('recommend/presurvey/survey/', views.survey, name='survey'),
    path('recommend/presurvey/', views.presurvey, name='presurvey'),
    path('recommend/', views.recommend, name='recommend'),
    path('search/', views.search, name='search'),
    path('search/filter', views.search_filter, name='search_filter'),
    path('detail_info/', views.detail_info, name='detail'),
    path('recommend/survey/submit/', views.survey_submit, name='survey_sub'),
]
