from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), # 게시판 리스트 URL
    path('post/<int:pk>/', views.post_detail, name='post_detail'), # 게시판 상세 페이지 URL
    path('post/new/', views.post_new, name='post_new'), # 게시판 추가 페이지 URL
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'), # 게시판 수정 페이지 URL
    path('draft/', views.post_draft_list, name='post_draft_list'), # 미 게시된 글목록 URL
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'), # 게시 기능 이벤트
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'), # 게시물 삭제 이벤트
]

#   <int:pk> -> 기본 키(primary key)에 해당되는 값을 찾아 뷰에 전달
#   ex) 3일 경우 index 3에 관한 데이터가 템플릿에 적용
