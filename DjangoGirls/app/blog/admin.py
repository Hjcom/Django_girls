from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)

# 관리자 패널에 모델을 등록하여 장고 관리자 페이지 사용 가능

