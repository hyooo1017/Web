"""myform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# 내서버로 바로 접속했을 때 Page not found(404)가 안뜨게!
# def root(request):
#     return redirect('articles:index')

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
    # 메인페이지 설정
    path('', lambda r: redirect('articles:index'), name='root')        # 주로 urls.py에는 함수를 따로 정의하지 않으므로 lambda로 연결
]

