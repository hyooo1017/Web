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
    # Article을 작성한 User -> article.user
    # User가 작성한 모든 Article -> user.article_set.all()

    # M:N (좋아요 기능) - User:Article
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')     # related_name으로 user가 작성한 기사와 좋아요 누른 기사 구분!
    # Article에 좋아요 누른 모든 User -> article.like_users.all()
    # User가 좋아요 누른 모든 Article -> user.like_articles.all()

# Auth
# 1. Authentication (인증)
# 2. Authorization (권한)