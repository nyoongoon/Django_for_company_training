from django.db import models

# Create your models here.
class Post(models.Model): # 데이터 베이스 모델로 만들어짐
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField