# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actor(models.Model):
    actor_id = models.BigAutoField(primary_key=True)
    movie_code = models.CharField(max_length=30)
    movie_name = models.CharField(max_length=100, blank=True, null=True)
    actor_name = models.CharField(max_length=30, blank=True, null=True)
    hit_grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actor'


class Company(models.Model):
    company_id = models.BigAutoField(primary_key=True)
    movie_code = models.CharField(max_length=30)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    company_type = models.CharField(max_length=30, blank=True, null=True)
    hit_grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class Genre(models.Model):
    genre_id = models.BigAutoField(primary_key=True)
    movie_code = models.CharField(max_length=30)
    genre_name = models.CharField(max_length=30, blank=True, null=True)
    hit_grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genre'


class Movie(models.Model):
    movie_code = models.CharField(primary_key=True, max_length=30)
    movie_name = models.CharField(max_length=100, blank=True, null=True)
    show_tm = models.BigIntegerField(blank=True, null=True)
    open_date = models.CharField(max_length=30, blank=True, null=True)
    type_name = models.CharField(max_length=30, blank=True, null=True)
    nation_name = models.CharField(max_length=30, blank=True, null=True)
    director = models.CharField(max_length=30, blank=True, null=True)
    watch_grade_name = models.CharField(max_length=30, blank=True, null=True)
    dist_name = models.CharField(max_length=100, blank=True, null=True)
    peak_yn = models.CharField(max_length=2, blank=True, null=True)
    genre = models.CharField(max_length=30, blank=True, null=True)
    hit_grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie'


class MovieAudi(models.Model):
    audi_id = models.BigAutoField(primary_key=True)
    movie_code = models.CharField(max_length=30)
    movie_name = models.CharField(max_length=100, blank=True, null=True)
    open_audi_cnt = models.BigIntegerField(blank=True, null=True)
    sec_audi_increase = models.FloatField(blank=True, null=True)
    hit_grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie_audi'
        unique_together = (('audi_id', 'movie_code'),)


class MovieHit(models.Model):
    movie_code = models.CharField(primary_key=True, max_length=30)
    movie_name = models.CharField(max_length=30, blank=True, null=True)
    tot_audi_cnt = models.BigIntegerField(blank=True, null=True)
    hit_grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie_hit'


class MovieRank(models.Model):
    rank_id = models.BigAutoField(primary_key=True)
    movie_code = models.ForeignKey(Movie, models.DO_NOTHING, db_column='movie_code')
    movie_name = models.CharField(max_length=100, blank=True, null=True)
    open_first_rank_yn = models.CharField(max_length=2, blank=True, null=True)
    sec_week_rank_drop = models.CharField(max_length=2, blank=True, null=True)
    hit_grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie_rank'
        unique_together = (('rank_id', 'movie_code'),)


class MovieSales(models.Model):
    sales_id = models.BigAutoField(primary_key=True)
    movie_code = models.ForeignKey(Movie, models.DO_NOTHING, db_column='movie_code')
    movie_name = models.CharField(max_length=100, blank=True, null=True)
    open_sales_share = models.FloatField(blank=True, null=True)
    avg_sales_share = models.FloatField(blank=True, null=True)
    tot_sales = models.BigIntegerField(blank=True, null=True)
    hit_grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie_sales'
        unique_together = (('sales_id', 'movie_code'),)


class MovieScore(models.Model):
    score_id = models.BigAutoField(primary_key=True)
    movie_code = models.ForeignKey(Movie, models.DO_NOTHING, db_column='movie_code')
    movie_name = models.CharField(max_length=100, blank=True, null=True)
    expe_score = models.FloatField(blank=True, null=True)
    audi_score = models.FloatField(blank=True, null=True)
    neti_score = models.FloatField(blank=True, null=True)
    hit_grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie_score'
        unique_together = (('score_id', 'movie_code'),)


class MovieScrn(models.Model):
    scrn_id = models.BigAutoField(primary_key=True)
    movie_code = models.ForeignKey(Movie, models.DO_NOTHING, db_column='movie_code')
    movie_name = models.CharField(max_length=100, blank=True, null=True)
    open_scrn_cnt = models.BigIntegerField(blank=True, null=True)
    avg_scrn_cnt = models.FloatField(blank=True, null=True)
    hit_grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie_scrn'
        unique_together = (('scrn_id', 'movie_code'),)


class MovieSearch(models.Model):
    search_id = models.BigAutoField(primary_key=True)
    movie_code = models.ForeignKey(Movie, models.DO_NOTHING, db_column='movie_code')
    movie_name = models.CharField(max_length=100, blank=True, null=True)
    first_search_ratio = models.FloatField(blank=True, null=True)
    second_search_ratio = models.FloatField(blank=True, null=True)
    third_search_ratio = models.FloatField(blank=True, null=True)
    hit_grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie_search'
        unique_together = (('search_id', 'movie_code'),)


class MovieShow(models.Model):
    show_id = models.BigAutoField(primary_key=True)
    movie_code = models.ForeignKey(Movie, models.DO_NOTHING, db_column='movie_code')
    movie_name = models.CharField(max_length=100, blank=True, null=True)
    open_show_cnt = models.BigIntegerField(blank=True, null=True)
    avg_show_cnt = models.FloatField(blank=True, null=True)
    hit_grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie_show'
        unique_together = (('show_id', 'movie_code'),)
