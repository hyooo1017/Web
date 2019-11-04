from django.db import models

# Create your models here.
class Movie(models.Model):
    # id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 50)               # 영화명
    title_en = models.CharField(max_length = 50)            # 영화명(영문)
    audience = models.IntegerField()                        # 누적 관객수
    open_date = models.DateTimeField()                      # 개봉일
    genre = models.CharField(max_length = 20)               # 장르
    watch_grade = models.CharField(max_length = 10)         # 관람등급
    score = models.FloatField()                             # 평점
    poster_url = models.TextField()                         # 포스터 이미지 URL
    description = models.TextField()                        # 영화 소개

    # def __str__(self):
    #     return f'{self.id}번 영화 - {self.title} : {self.score}' 