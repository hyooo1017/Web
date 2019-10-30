from django.db import models

# Create your models here.
class Student(models.Model):
    # id = models.AutoField(primary_key = True)             -> 자동으로 추가되기 때문에 따로 작성하지 않음
    name = models.CharField(max_length = 10)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.id}번 학생 - {self.name} : {self.age}' 