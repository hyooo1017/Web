from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.index, name='index'), # GET /students/
    path('new/', views.new, name='new'), # GET,POST / students/new/
#   path('create/', views.create, name='create'), # POST /students/create/ (X) -> create가 자원이 아닌 행위여서
    path('<int:pk>/', views.detail, name='detail'), # GET /students/1/
    path('<int:pk>/delete/', views.delete, name='delete'), # POST /students/1/delete/
    path('<int:pk>/edit/', views.edit, name='edit'), # GET /students/1/edit/
#   path('<int:pk>/update/', views.update, name='update'), # POST /students/1/update/ (X) -> update도 자원이 아니고 행위이므로
    path('<int:student_pk>/comments/new/', views.comments_new, name='comments_new'),
    path('<int:student_pk>/comments/<int:pk>/delete/', views.comments_delete, name='comments_delete'), # POST /students/1/comments/1/delete/
    path('<int:student_pk>/comments/<int:pk>/edit/', views.comments_edit, name='comments_edit'),
]

# URL Name
# path('주소/', view.함수, name='이름)
# {% url 'new' %}로 작성하면 /students/new/와 같은 기능 동작
# [ 장점 ]
# 1. 주소의 변경이 필요할 때, urls.py에서만 수정해주면 됨
# 2. 마지막 '/'를 빠뜨리는 실수를 차단할 수 있음

# App Name - 특정 app의 urls.py 자체
# {% url 'app_name:path_name' %} => 주소


# RESTful
# 1. 자원(Resource) - URL
# 2. 행위(Verb) - HTTP Method (GET, POST, ...)
# 3. 표현(Representation) - 자원 + 행위


# Django는 PUT/PATCH/DELETE 불가능, 따라서...
# GET  /students/2/edit/  => 수정 페이지 보여줌
# POST /students/2/edit/  => 수정 작업 수행

# ex)
# GET /users/1 => user 1번 가져옴
# PUT /users/1 => user 1번 수정
# DELETE /users/1 => user 1번 삭제