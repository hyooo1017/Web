from django.db import models

# M:N
# 1. Doctor : Patien (1:N)
# 2. Doctor : Reservation : Patien (1:N + 1:N)
# 3. Doctor : Patient (M:N) - Reservation(조인 테이블) 사용
# 4. Doctor : Patient (M:N) - Reservation 사용 안함

class Doctor(models.Model):
    name = models.CharField(max_length=20)

class Patient(models.Model):
    name = models.CharField(max_length=20)
    # doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    # doctors = models.ManyToManyField(Doctor, through='Reservation')
    doctors = models.ManyToManyField(Doctor, related_name='patients') # related_name은 의사측에서 환자를 부를 때 사용할 이름 정의

# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete = models.CASCADE)