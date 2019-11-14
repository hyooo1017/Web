from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    articles = Article.objects.all()
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
        # 1. 넘어온 데이터를 받기
        article_form = ArticleForm(request.POST)

        # 2. 넘어온 데이터 검증
        if article_form.is_valid():
            # 3. 데이터베이스에 Article 만들기!
            article = article_form.save()

            # 4. redirect -> detail
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm()

    # 폼을 보여줌
    context = {
        'article_form': article_form,
    }
    return render(request, 'articles/new.html', context)

@login_required
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