from django.db import models
from django.conf import settings        # user 모델에 대한 정보가 저장되어 있음

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 1:N (User:Article)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 장고에서 권장되는 방법 -> 다른 유저를 사용할 수도 있어서 (호환성 문제?)

# Auth
# 1. Authentication (인증)
# 2. Authorization (권한)