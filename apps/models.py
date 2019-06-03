from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    content = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'articles'


class Books(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    autho = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'books'


class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'course'


class Lst(models.Model):
    a = models.IntegerField(blank=True, null=True)
    b = models.IntegerField(blank=True, null=True)
    c = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lst'


class SC(models.Model):
    id = models.IntegerField(primary_key=True)
    sid = models.ForeignKey('Student', models.DO_NOTHING, db_column='sid', blank=True, null=True)
    cid = models.ForeignKey(Course, models.DO_NOTHING, db_column='cid', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 's_c'


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    sname = models.CharField(max_length=20, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'student'


class T1(models.Model):
    name = models.ForeignKey('T2', models.DO_NOTHING, blank=True, null=True)
    kechen = models.CharField(max_length=20, blank=True, null=True)
    femshu = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't1'


class T2(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't2'
