"""intro URL Configuration

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

# 어떤 주소로 접근할 때 어떤 내용을 보여줄건지 정의
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # pages에 있는 views
    path('index/', views.index),     # 플라스크에서 @app.route와 동일한 부분
    path('dinner/', views.dinner),
    path('hello/<str:name>/', views.hello),
    path('introduce/<str:name>/<int:age>/', views.introduce),
    path('multiple/<int:num1>/<int:num2>/', views.multiple),
    path('dtl/', views.dtl),
    path('birthday/', views.birthday),
]
