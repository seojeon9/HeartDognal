# from django.shortcuts import render
from datetime import date, datetime, timedelta
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_api.models import *
from rest_api.serializers import *
from django.http import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Parameter, IN_QUERY, TYPE_STRING


# Create your views here.
def get_queryset_by_date(model, query_params):
    if ~('start_date' in query_params) and ~('end_date' in query_params):
        queryset = model.objects.filter(
            std_day__gt=(datetime.today() - timedelta(7)))

    if 'start_date' in query_params and 'end_date' in query_params:
        start_date = query_params['start_date']
        end_date = query_params['end_date']
        queryset = model.objects.filter(std_day__range=(
            date.fromisformat(start_date), date.fromisformat(end_date)))

    if 'start_date' in query_params:
        start_date = query_params['start_date']
        queryset = model.objects.filter(std_day__gt=start_date)

    if 'end_date' in query_params:
        end_date = query_params['end_date']
        queryset = model.objects.filter(std_day__lt=end_date)

    return queryset

# SAMPLE

class MovieActorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = MovieActorSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="영화코드 별 영화이름, 배우이름, 흥행등급 목록 반환",
        operation_description="영화 제목을 입력하면 데이터를 반환합니다",
        manual_parameters=[
            Parameter("movie_name", IN_QUERY, type=TYPE_STRING,
                      description="영화 제목, (required : False)", required=False),
        ],
    )
    def list(self, request):
        query_params = request.query_params
        movie_parm = query_params['movie_name']
        queryset = Actor.objects.filter(movie_name__contains=movie_parm)
        print('params : >>>>>>>>>>>>>>>>>>>> ', query_params)
        serializers = self.get_serializer(queryset, many=True)
        return JsonResponse(serializers.data, safe=False)

    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request):
        pass


class MovieCompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    serializer_class = MovieCompanySerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="영화코드 별 영화사이름, 영화사종류, 흥행등급 목록 반환",
        operation_description=" ",
        manual_parameters=[
            Parameter("hit_grade", IN_QUERY, type=TYPE_STRING,
                      description="영화 흥행 등급, (required : False)", required=False),
        ],
    )
    def list(self, request):
        query_params = request.query_params
        queryset = Company.objects.filter(hit_grade__contains = query_params['hit_grade'] )
        print('params : >>>>>>>>>>>>>>>>>>>> ', query_params)
        serializers = self.get_serializer(queryset, many=True)
        return JsonResponse(serializers.data, safe=False)

    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request):
        pass


class MovieGenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = MovieGenreSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="영화코드 별 장르이름, 흥행등급 목록 반환",
        operation_description=" ",
        manual_parameters=[
            Parameter("genre_name", IN_QUERY, type=TYPE_STRING,
                      description="장르, (required : False)", required=False),
        ],
    )
    def list(self, request):
        query_params = request.query_params
        queryset = Genre.objects.filter(genre_name__contains = query_params['genre_name'] )
        print('params : >>>>>>>>>>>>>>>>>>>> ', query_params)
        serializers = self.get_serializer(queryset, many=True)
        return JsonResponse(serializers.data, safe=False)

    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request):
        pass


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="영화 별 상영시간, 개봉일, 영화 유형명, 제작국가, 영화감독명, 관람등급명, 배급사, 성수기여부, 대표장르, 흥행등급 반환",
        operation_description=" ",
        manual_parameters=[
            Parameter("hit_grade", IN_QUERY, type=TYPE_STRING,
                      description="영화 흥행 등급, (required : False)", required=False),
        ],
    )
    def list(self, request):
        query_params = request.query_params
        queryset = Movie.objects.filter(hit_grade__contains = query_params['hit_grade'] )
        print('params : >>>>>>>>>>>>>>>>>>>> ', query_params)
        serializers = self.get_serializer(queryset, many=True)
        return JsonResponse(serializers.data, safe=False)

    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request):
        pass


class MovieAudiViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MovieAudi.objects.all()
    serializer_class = MovieAudiSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="영화 별 개봉일 관객수, 2주차관객수증가율, 흥행등급 반환",
        operation_description=" ",
        manual_parameters=[
            Parameter("hit_grade", IN_QUERY, type=TYPE_STRING,
                      description="영화 제목, (required : False)", required=False),
        ],
    )
    def list(self, request):
        query_params = request.query_params
        queryset = MovieAudi.objects.filter(hit_grade__contains = query_params['hit_grade'] )
        print('params : >>>>>>>>>>>>>>>>>>>> ', query_params)
        serializers = self.get_serializer(queryset, many=True)
        return JsonResponse(serializers.data, safe=False)

    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request):
        pass


class MovieHitViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MovieHit.objects.all()
    serializer_class = MovieHitSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="영화별 총관객수, 흥행등급 반환",
        operation_description=" ",
        manual_parameters=[
            Parameter("hit_grade", IN_QUERY, type=TYPE_STRING,
                      description="영화 흥행 등급, (required : False)", required=False),
        ],
    )
    def list(self, request):
        query_params = request.query_params
        queryset = MovieHit.objects.filter(hit_grade__contains = query_params['hit_grade'] )
        print('params : >>>>>>>>>>>>>>>>>>>> ', query_params)
        serializers = self.get_serializer(queryset, many=True)
        return JsonResponse(serializers.data, safe=False)

    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request):
        pass


class MovieRankViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MovieRank.objects.all()
    serializer_class = MovieRankSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="영화별 개봉일 1위 여부, 2주차순위하락여부, 흥행등급 반환",
        operation_description=" ",
        manual_parameters=[
            Parameter("hit_grade", IN_QUERY, type=TYPE_STRING,
                      description="영화 제목, (required : False)", required=False),
        ],
    )
    def list(self, request):
        query_params = request.query_params
        queryset = MovieRank.objects.filter(hit_grade__contains = query_params['hit_grade'] )
        print('params : >>>>>>>>>>>>>>>>>>>> ', query_params)
        serializers = self.get_serializer(queryset, many=True)
        return JsonResponse(serializers.data, safe=False)

    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request):
        pass


class MovieSalesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MovieSales.objects.all()
    serializer_class = MovieSalesSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="영화별 개봉일매출점유율, 평균매출점유율, 총매출액, 흥행등급 반환",
        operation_description=" ",
        manual_parameters=[
            Parameter("hit_grade", IN_QUERY, type=TYPE_STRING,
                      description="영화 제목, (required : False)", required=False),
        ],
    )
    def list(self, request):
        query_params = request.query_params
        queryset = MovieSales.objects.filter(hit_grade__contains = query_params['hit_grade'] )
        print('params : >>>>>>>>>>>>>>>>>>>> ', query_params)
        serializers = self.get_serializer(queryset, many=True)
        return JsonResponse(serializers.data, safe=False)

    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request):
        pass


class MovieScoreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MovieScore.objects.all()
    serializer_class = MovieScoreSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="영화 별 전문가평점, 관람객평점, 네티즌평점, 흥행등급 반환",
        operation_description=" ",
        manual_parameters=[
            Parameter("hit_grade", IN_QUERY, type=TYPE_STRING,
                      description="영화 제목, (required : False)", required=False),
        ],
    )
    def list(self, request):
        query_params = request.query_params
        queryset = MovieScore.objects.filter(hit_grade__contains = query_params['hit_grade'] )
        print('params : >>>>>>>>>>>>>>>>>>>> ', query_params)
        serializers = self.get_serializer(queryset, many=True)
        return JsonResponse(serializers.data, safe=False)

    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request):
        pass


class MovieScrnViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MovieScrn.objects.all()
    serializer_class = MovieScrnSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="영화 별 개봉일스크린수, 평균스크린수, 흥행등급 반환",
        operation_description=" ",
        manual_parameters=[
            Parameter("hit_grade", IN_QUERY, type=TYPE_STRING,
                      description="영화 제목, (required : False)", required=False),
        ],
    )
    def list(self, request):
        query_params = request.query_params
        queryset = MovieScrn.objects.filter(hit_grade__contains = query_params['hit_grade'] )
        print('params : >>>>>>>>>>>>>>>>>>>> ', query_params)
        serializers = self.get_serializer(queryset, many=True)
        return JsonResponse(serializers.data, safe=False)
    

    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request):
        pass



class MovieSearchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MovieSearch.objects.all()
    serializer_class = MovieSearchSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="영화별 1, 2, 3주차 검색비율, 흥행등급 반환",
        operation_description=" ",
        manual_parameters=[
            Parameter("hit_grade", IN_QUERY, type=TYPE_STRING,
                      description="영화 제목, (required : False)", required=False),
        ],
    )
    def list(self, request):
        query_params = request.query_params
        queryset = MovieSearch.objects.filter(hit_grade__contains = query_params['hit_grade'] )
        print('params : >>>>>>>>>>>>>>>>>>>> ', query_params)
        serializers = self.get_serializer(queryset, many=True)
        return JsonResponse(serializers.data, safe=False)

    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request):
        pass


class MovieShowViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MovieShow.objects.all()
    serializer_class = MovieShowSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="영화 별 개봉일생영횟수, 평균상영횟수, 흥행등급 반환",
        operation_description=" ",
        manual_parameters=[
            Parameter("hit_grade", IN_QUERY, type=TYPE_STRING,
                      description="영화 제목, (required : False)", required=False),
        ],
    )
    def list(self, request):
        query_params = request.query_params
        queryset = MovieShow.objects.filter(hit_grade__contains = query_params['hit_grade'] )
        print('params : >>>>>>>>>>>>>>>>>>>> ', query_params)
        serializers = self.get_serializer(queryset, many=True)
        return JsonResponse(serializers.data, safe=False)

    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request):
        pass
