# views.py : 모델에서 필요한 정보를 받아와서 템플릿에 전달하는 역할을 함.

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


# 게시판 리스트
def post_list(request):
    # 장고는 페이지가 요청되면 요청에 대한 메타데이터를 포함하는 객체 HttpRequest 객체를 생성함
    # HttpRequest 객체는 뷰 함수의 첫번쨰 인수로 전달한다.(request = HttpRequest 객체)

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # 게시일(published_date)로 과거에 작성한 글을 내림차순으로 정렬
    # 장고 ORM은 필드이름과 연산자를 밑줄 2개를 사용해 구분한다. (lte : 같거나 보다 작다)
    return render(request, 'blog/post_list.html', {'posts': posts})

# render(httpRequest 객체, 템플릿명, 문자열(딕셔너리형))
# render 함수는 템플릿랜더링을 하기 위한 함수이며 각 뷰는 HttpResponse 객체를 반환하는데
# render 함수의 리턴값도 HttpResponse(랜더링된 텍스트값)이다.

# 게시판 추가
@login_required
def post_new(request):
    if request.method == 'POST':
       form = PostForm(request.POST)
    # 폼에서 데이터를 POST 방식으로 submit 했을 경우 템플릿에 입력했던 데이터를 PostForm 으로 전달
    # request.POST : 템플릿에 입력했던 데이터
       if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
       # is_valid() : POST 데이터로 잘못된 데이터가 전달되었는지 체크/ 정상적이면 True 리턴
       # commit=False : 넘겨진 데이터를 바로 POST 모델에 저장하지 않기 위해 적용 / 작성자와 추가한 날짜시간을 추가한 다음 저장해야 되기 때문
       # redirect('템플릿', pk=post.pk) : 해당 기본 키에 속한 데이터의 뷰로 이동
    else:
        form = PostForm()
    # POST 방식으로 submit 안했을 경우 == 처음 페이지에 접속했을 경우므로 새 글을 쓸 수 있도록 폼 초기화
    return render(request, 'blog/post_edit.html', {'form': form})

# 상세 페이지
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # get_object_or_404(모델명, 조건)
    # get() 함수를 이용하여 모델은 호출한다. 해당 조건에 해당되는 오브젝트가 존재하지 않을 경우 http404예외 발생
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        # 템플릿에 입력했던 데이터와 해당 기본키에 해당되는 인스턴스를 PostForm 으로 전달
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        # 처음 페이지에 접속했을 경우 기본 키에 해당되는 인스턴스를 PostForm으로 전달, 텍스트박스에 해당 데이터 출력
    return render(request, 'blog/post_edit.html', {'form': form})

# 미게시된 글목록 템플릿 랜더링
@login_required
def post_draft_list(request):
    # 게시한 날짜가 없을경우 내림차순으로 정렬
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

# 게시물 게시 메소드
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # models.py publish() 참고
    post.publish()
    return redirect('post_detail', pk=pk)

# 게시물 삭제 메소드
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # 해당 데이터 삭제
    post.delete()
    return redirect('post_list')

