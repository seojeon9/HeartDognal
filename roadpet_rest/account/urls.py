from django.core.checks.templates import check_for_template_tags_with_the_same_name
from django.urls import path

# 장고가 제공하는 계정과 관련된 view import
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'

urlpatterns = [
    path('login/',  auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('login_bi/', views.get_token, name='login_bi'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('apikey/', views.get_apikey, name='apikey'),
]
