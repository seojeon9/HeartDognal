from rest_framework import serializers
from rest_api.models import Actor, Company, Genre, Movie, MovieAudi, MovieHit, MovieRank, MovieSales, MovieScore, MovieScrn, MovieSearch, MovieShow

class MovieActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ['actor_id', 'movie_code', 'movie_name', 'actor_name', 'hit_grade']


class MovieCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['company_id', 'movie_code', 'company_name', 'company_type', 'hit_grade']


class MovieGenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['genre_id', 'movie_code', 'genre_name', 'hit_grade']


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['movie_code', 'movie_name', 'show_tm', 'open_date', 'type_name', 'nation_name', 'director', 'watch_grade_name', 'dist_name', 'peak_yn', 'genre', 'hit_grade']


class MovieAudiSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieAudi
        fields = ['audi_id', 'movie_code', 'movie_name', 'open_audi_cnt', 'sec_audi_increase', 'hit_grade']


class MovieHitSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieHit
        fields = ['movie_code', 'movie_name', 'tot_audi_cnt', 'hit_grade']


class MovieRankSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieRank
        fields = ['rank_id', 'movie_code', 'movie_name', 'open_first_rank_yn', 'sec_week_rank_drop', 'hit_grade']


class MovieSalesSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieSales
        fields = ['sales_id', 'movie_code', 'movie_name', 'open_sales_share', 'avg_sales_share', 'tot_sales', 'hit_grade']


class MovieScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieScore
        fields = ['score_id', 'movie_code', 'movie_name', 'expe_score', 'audi_score', 'neti_score', 'hit_grade']


class MovieScrnSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieScrn
        fields = ['scrn_id', 'movie_code', 'movie_name', 'hit_grade', 'open_scrn_cnt', 'avg_scrn_cnt']


class MovieSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieSearch
        fields = ['search_id', 'movie_code', 'movie_name', 'first_search_ratio', 'second_search_ratio', 'third_search_ratio', 'hit_grade']


class MovieShowSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieShow
        fields = ['show_id', 'movie_code', 'movie_name', 'open_show_cnt', 'avg_show_cnt', 'hit_grade']
