# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime
from django.utils.dateformat import DateFormat


class AdoptionInquiry(models.Model):
    ai_id = models.BigAutoField(primary_key=True)
    username = models.BigIntegerField()
    desertion_no = models.BigIntegerField(blank=True, null=True)
    std_date = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adoption_inquiry'


class LikeStarPet(models.Model):
    lp_id = models.BigAutoField(primary_key=True)
    username = models.BigIntegerField()
    desertion_no = models.BigIntegerField(blank=True, null=True)
    star = models.BigIntegerField(blank=True, null=True)
    std_date = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'like_star_pet'


class RoaddogInfo(models.Model):
    desertion_no = models.BigIntegerField(primary_key=True)
    happen_dt = models.CharField(max_length=100, blank=True, null=True)
    happen_place = models.CharField(max_length=200, blank=True, null=True)
    kind_nm = models.CharField(max_length=100, blank=True, null=True)
    color_nm = models.CharField(max_length=100, blank=True, null=True)
    age = models.CharField(max_length=100, blank=True, null=True)
    weight = models.CharField(max_length=100, blank=True, null=True)
    profile = models.CharField(max_length=200, blank=True, null=True)
    process_st = models.CharField(max_length=100, blank=True, null=True)
    sex_cd = models.CharField(max_length=10, blank=True, null=True)
    neuter_yn = models.CharField(max_length=10, blank=True, null=True)
    special_mark = models.CharField(max_length=200, blank=True, null=True)
    care_id = models.BigIntegerField()
    label = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roaddog_info'


class Shelter(models.Model):
    st_cd = models.BigIntegerField(primary_key=True)
    care_nm = models.CharField(max_length=100, blank=True, null=True)
    addr_detail = models.CharField(max_length=500, blank=True, null=True)
    care_tel = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.CharField(max_length=100, blank=True, null=True)
    sigungu_cd = models.BigIntegerField()
    care_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'shelter'


class Sido(models.Model):
    sido_cd = models.BigIntegerField(primary_key=True)
    sido_nm = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sido'


class Sigungu(models.Model):
    sigungu_cd = models.BigIntegerField(primary_key=True)
    sigungu_nm = models.CharField(max_length=100, blank=True, null=True)
    sido_cd = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'sigungu'


class Survey(models.Model):
    sv_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    weight_cd = models.BigIntegerField(blank=True, null=True)
    age_cd = models.BigIntegerField(blank=True, null=True)
    attr_cd = models.BigIntegerField(blank=True, null=True)
    health_cd = models.BigIntegerField(blank=True, null=True)

    std_date = models.CharField(
        max_length=100, blank=True, null=True, default=DateFormat(datetime.now()).format('Ymd'))

    class Meta:
        managed = False
        db_table = 'survey'


class Kind(models.Model):
    kind_cd = models.BigIntegerField(primary_key=True)
    kind_nm = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kind'
