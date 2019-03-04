# ModelForm 장고 기본 폼 정의파일

from django import forms
# 기본 장고 폼 모델 import
from .models import Post, Comment
# Post 모델 import

class PostForm(forms.ModelForm):
# 장고 기본 폼 정의 / 폼 name : PostForm

    class Meta:
        model = Post
        fields = ('title', 'text',)

# data는 Post 모델 사용. 폼에 보여질 필드 정의

# Comment 모델 기반 폼
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)