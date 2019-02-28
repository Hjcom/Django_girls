from django.contrib import admin
from django.urls import path, include


from django.contrib.auth import views


urlpatterns = [
    path('admin/', admin.site.urls), # 관리자 페이지

    # 기본 로그인 뷰 호출(템플릿명은 registration/login.html이 기본값이므로 생략해도 됨)
    path('accounts/login/', views.LoginView.as_view(), name='login'),

    # 기본 로그아웃 뷰 호출 / as_views() 사용하면 kwargs 속성은 검사하지 않으므로 naxt_page 속성값을 사용함
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),

    # 처음 페이지를 메인페이지를 들어갈때 blog/urls.py의 영향을 받는다.
    path('', include('blog.urls')),
]


# 1.x 버전에선
# path('accounts/login/', views.login, name='login'),
# path('accounts/logout/', views.logout, name='logout', kwargs={'next_page': '/'}),

# 장고 로그인, 로그아웃 뷰 내용은
# https://docs.djangoproject.com/en/2.1/topics/auth/default/ 참고할것
