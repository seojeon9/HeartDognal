"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from rest_api import views as rest_view
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from . import views


router = routers.DefaultRouter()

router.register(r'movie/movie_actor', rest_view.MovieActorViewSet)

router.register(r'movie/movie_company', rest_view.MovieCompanyViewSet)

router.register(r'movie/movie_genre', rest_view.MovieGenreViewSet)

router.register(r'movie/movie_movie', rest_view.MovieViewSet)

router.register(r'movie/movie_movie_audi', rest_view.MovieAudiViewSet)

router.register(r'movie/movie_moviehit', rest_view.MovieHitViewSet)

router.register(r'movie/movie_movie_rank', rest_view.MovieRankViewSet)

router.register(r'movie/movie_movie_sales', rest_view.MovieSalesViewSet)

router.register(r'movie/movie_movie_score', rest_view.MovieScoreViewSet)

router.register(r'movie/movie_movie_scrn', rest_view.MovieScrnViewSet)

router.register(r'movie/movie_movie_search', rest_view.MovieSearchViewSet)

router.register(r'movie/movie_movie_show', rest_view.MovieShowViewSet)



# urlpatterns = [
#     # path('admin/', admin.site.urls),
#     path('', include(router.urls)),
# ]

schema_view = get_schema_view(
    openapi.Info(
        title="MOVIE_API",
        default_version='v2',
        description="MOVIE_API",
    ),
    public=True,
)


urlpatterns = [
    path('', views.index),
    path('', include(router.urls)),
    path('accounts/', include('account.urls')),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='doc'),
]