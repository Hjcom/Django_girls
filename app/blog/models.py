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

    # 댓글 승인된 것만 정렬해서 출력
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.text


# 댓글 모델
class Comment(models.Model):
    # related_name : 기존 모델의 어트리뷰트(칼럼)의 이름 말고 다른 이름으로 지정할 수 있게 해주는 속성
    # Post 모델의 외래키
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='comments')

    # 사용자명
    author = models.CharField(max_length=200)
    # 댓글내용
    text = models.TextField()
    # 게시날짜
    created_date = models.DateTimeField(default=timezone.now)
    # 댓글 승인 여부
    approved_comment = models.BooleanField(default=False)

    # 댓글 승인 메소드
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

