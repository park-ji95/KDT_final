from django.db import models

class Hospital(models.Model):
    type=models.TextField(max_length=255)
    hospital=models.IntegerField()
    doctor=models.IntegerField()


class Population(models.Model):
    age = models.TextField()
    total = models.IntegerField()
    m = models.IntegerField()
    f = models.IntegerField()

class Medicalinfo(models.Model):
    type = models.TextField()
    hospital = models.IntegerField()
    doctor = models.IntegerField()
    nurse = models.IntegerField()
    patient = models.IntegerField()

class Counts(models.Model):
    region=models.TextField()
    clinic=models.IntegerField()
    healthcenter=models.IntegerField()
    pharmacy = models.IntegerField()
    dentist = models.IntegerField()
    oriental = models.IntegerField()


class Sejong(models.Model):
    #no = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(max_length=100)  # Field renamed to remove unsuitable characters.
    type = models.TextField()  # Field renamed to remove unsuitable characters.
    phone = models.TextField()
    code = models.IntegerField()
    address = models.TextField()
    address1 = models.TextField()
    department = models.TextField()


class Doctor(models.Model):
    department = models.TextField()  # 진료과목별
    sum = models.IntegerField()  # 합계
    genhos = models.IntegerField()  # 종합병원
    hos = models.IntegerField()  # 병원
    nurs = models.IntegerField()  # 요양병원
    mental = models.IntegerField()  # 정신병원
    clinic = models.IntegerField()  # 의원
    Public = models.IntegerField()  # 보건지소

