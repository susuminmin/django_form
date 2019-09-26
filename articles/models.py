from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # 메타 클래스(데이터를 위한 데이터)
    class Meta:
        ordering = ('-pk',) # 마지막 생성된 것이 가장 첫번째 오도록

    def __self__(self):
        return f'{self.pk} - {self.title}'
