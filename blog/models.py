from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200) # 짧은 글자 데이터
    content = models.TextField() # 긴 글
    created_at = models.DateTimeField(auto_now_add=True) # 글 작성 시간 자동 저장

    def __str__(self):
        return self.title # 작성한 title로 표시하게 해줌