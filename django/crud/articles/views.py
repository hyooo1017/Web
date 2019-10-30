from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('-id')    # => Query Set ~= List

    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 넘어온 데이터 받기
    # 이유 2번 - GET(URL), POST(HTTP body)
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article.objects.create(title = title, content = content)
    # article.title이나 article.content로 확인 가능
    return redirect(f'/articles/{article.pk}/')

def detail(request, pk):
    article = Article.objects.get(pk=pk)
       
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    context = {
        'article' : article,
    }
    return redirect('/articles/')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    # 1. pk에 해당하는 article 가져오기
    article = Article.objects.get(pk=pk)

    # 2. edit로부터 넘어온 데이터 가져오기
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # 3. 넘어온 데이터를 article에 새롭게 저장
    article.title = title
    article.content = content
    article.save()

    context = {
        'article' : article,
    }
    return redirect(f'/articles/{article.pk}/')     # detail 페이지로 redirect

