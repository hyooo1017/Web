from django.shortcuts import render

# Create your views here.
def index(request):
    # 'index.html'로 경로를 설정하면 settings.py의 INSTALLED_APPS의 순서에 따라
    # utils보다 더 위에 경로 설정되어 있는 pages의 templates 폴더 안에 있는 index가 경로로 잡힘
    return render(request, 'utils/index.html')