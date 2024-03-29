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
from django.urls import path, include

# settings.py 안의 INSTALLED_APPS에 작성된 순서대로 경로 작성
urlpatterns = [
    path('pages/', include('pages.urls')),
    path('utils/', include('utils.urls')),
    path('admin/', admin.site.urls),
]