from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    article_list = Article.objects.all()

    # Pagination
    # 1. articles를 Paginator에 입력
    paginator = Paginator(article_list, 3)      # 첫 번째 파라미터는 가져온 데이터, 두 번째 파라미터는 몇 개씪 보여줄건지
    # 2. 몇 번째 page를 보여줄건지 GET으로 가져옴
    page = request.GET.get('page')
    # 3. 해당하는 page의 articles만 보기
    articles = paginator.get_page(page)
    

    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# new함수에 접근할 때 먼저 로그인 되어 있는지 확인
# 만일 로그인되어 있지 않다면 로그인 페이지로 자동으로 넘어감
# 그 때 주소에서 next값으로 로그인 확인을 요구했던 페이지를 값으로 갖고 있음
@login_required
def new(request):
    if request.method == 'POST':
        # 데이터베이스에 데이터 생성 (ModelForm)
        # 1. 넘어온 데이터를 받기 (title, content만 있음)
        article_form = ArticleForm(request.POST)

        # 2. 넘어온 데이터 검증
        if article_form.is_valid():
            # 3. 데이터베이스에 Article 만들기!
            article = article_form.save(commit=False)       # 데이터베이스에 바로 저장되지 않음 ( article 인스턴스만 만들어짐 )
            # 3-1. user 정보 끼워넣기
            article.user = request.user
            article.save()
            # 4. redirect -> detail
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm()

    # 폼을 보여줌
    context = {
        'article_form': article_form,
    }
    return render(request, 'articles/new.html', context)

def detail(request, pk):
    # 1. pk번째 데이터를 가져오기
    article = Article.objects.get(pk=pk)
    # 2. context로 넘겨주기
    context = {
        'article': article,
    }
    # 3. render와 함께 html로 넘겨주기
    return render(request, 'articles/detail.html', context)

@login_required
def edit(request, pk):
    article = Article.objects.get(pk=pk)

    # article의 작성자인지 검증
    if request.user != article.user:
        return redirect('articles:detail', article.pk)

    if request.method == 'POST':
        # Article 수정
        # 1. 넘어온 데이터 받기
        article_form = ArticleForm(request.POST, instance=article)
        # 2. 데이터 검증
        if article_form.is_valid():
            # 3. 검증된 데이터로 수정 & 저장
            article_form.save()

            # 4. redirect -> detail
            return redirect('articles:detail', article.pk)
    else:
        # Article 수정하는 Form 보여주기
        article_form = ArticleForm(instance=article)

    context = {
        'article_form': article_form,
    }
    return render(request, 'articles/new.html', context)

# POST 요청만 받음
@login_required
def like(request, pk):
    # 1. pk번 article 가져오기
    article = Article.objects.get(pk=pk)
    # 2. 현재 로그인한 User가 이 article에 좋아요를 눌렀는지?
    if request.user in article.like_users.all():
        # 3-1. 좋아요 취소
        article.like_users.remove(request.user)
    else:
        # 3-2. 좋아요
        article.like_users.add(request.user)
    return redirect('articles:detail', article.pk)

# GET 요청을 받음
def search(request):
    
    # 1. request로부터 검색어 가져오기
    query = request.GET.get('query')    # => 'asdf'
    # Article에서 검색어가 title에 있는지 찾기
    articles = Article.objects.filter(title__contains=query)       # _ 2개! -> 검색어를 포함하고 있는 title 찾기
    # title__icontains -> 대소문자 구분 (장고는 sqlite를 사용하기 때문에 대소문자 구분 불가)
    
    # 3. context로 결과값 template에 넘겨주기
    context = {
        'articles': articles,
    }
    return render(request, 'articles/search.html', context)