from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # models.ForeignKey : 다른 모델에 대한 링크
    title = models.CharField(max_length=200)
    # models.CharField : 글자 수가 제한된 텍스트를 정의
    text = models.TextField()
    # models.TextField : 글자 수에 제한이 없는 긴 텍스트 속성
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # models.DateTimeField : 날짜와 시간을 의미합니다.

    # 게시한 날짜시간 적용 후 데이터 저장
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text