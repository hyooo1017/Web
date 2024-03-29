from django.shortcuts import render
import random

# Create your views here.
# 플라스크는 함수 인자가 없어도 됬는데
# 장고에서는 request를 첫 번째 파라미터로 받음
def index(request):

    context = {
        'name' : 'nwith',
    }       # 변수명은 크게 상관 없음, 튜플 형태만 지켜지면!

    return render(request, 'pages/index.html', context)    # render함수를 사용해 html로 보여줌

# Template Variable
def dinner(request):
    foods = ['초밥', '카레', '칼국수', '치킨', '김치찌개']
    pick = random.choice(foods)
    context = {
        'pick' : pick,
    }
    return render(request, 'pages/dinner.html', context)

# Variable Routing
def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'pages/hello.html', context)

# 실습
# 1. '이름'과 '나이'를 Variable Routing'을 통해 받아서 자기소개
def introduce(request, name, age):
    context = {
        'name' : name,
        'age' : age,
    }
    return render(request, 'pages/introduce.html', context)

# 2. 숫자 2개를 Variable Routing을 통해 받아 곱셈 결과 보여주기
def multiple(request, num1, num2):
    result = num1 * num2  # context 내부에서 실행해도 됨
    context = {
        'num1' : num1,
        'num2' : num2,
        'result' : result, # 'result' : num1 * num2
    }
    return render(request, 'pages/multiple.html', context)

from datetime import datetime

def dtl(request):
    foods = ['짜장면', '짬뽕', '냉면', '우동']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []

    context = {
        'foods' : foods,
        'my_sentence' : my_sentence,
        'messages' : messages,
        'datetimenow' : datetimenow,
        'empty_list' : empty_list,
    }
    return render(request, 'pages/dtl.html', context)

# 실습
# Is it your birthday?
# 오늘이 자신의 생일이면 '예'를, 아니면 '아니오'를 보여주는 페이지
def birthday(request):
    today = datetime.now()

    # if today.month == 10 and today.day ==17:
    #     result = True
    # else:
    #     result = False

    result = today.month == 10 and today.day ==17

    context = {
        'result' : result
    }
    return render(request, 'pages/birthday.html', context)


# From Tag - <from>
# 웹에서 사용자의 정보를 입력받는 방식을 제공
# 사용자로부터 받은 데이터를 서버로 전송하는 역할
# 1. action - 입력받은 데이터가 전송될 URL
# 2. method - 데이터 전달 방식 (기본값 'GET')
# 
# Input Tag - <input>
# 1. type - 사용자로부터 어떠한 자료형으로 받을지
# 2. name - 데이터를 전송할 때, 어떠한 이름으로 전송할지
# GET -> ?key1=value1&key2=value2 (쿼리스트링)
# 
# # Label Tag - <label>
# # Input 양식에 이름을 붙일 때 
# 1. for - input과 연결. 'id'를 사용.

def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    #request.GET => {'message' : '안녕', 'message2' : '잘가'}
    message = request.GET.get('message')        # => '안녕'
    message2 = request.GET.get('message2')      # => '잘가'
    context = {
        'message' : message,
        'message2' : message2,
    }
    return render(request, 'pages/catch.html', context)

# 실습
# 로또 번호 생성기
# 사용자로부터 번호 몇 개를 생성할지를 입력받고,
# 그 갯수만큼 로또 번호 번호를 보여주기
# ex) 5 -> 5줄의 로또 번호 세트
def lotto(request):
    return render(request, 'pages/lotto.html')

def generate(request):
    # request.GET => {'count' : 5}
    count = int(request.GET.get('count'))    # => 5

    lotto_numbers = range(1, 46)
    my_lottos = []

    for n in range(count):
        sorted_lotto = sorted(random.sample(lotto_numbers, 6))
        my_lottos.append(sorted_lotto)     # => [...]

    context = {
        'my_lottos' : my_lottos,
        'count' : count,
    }
    return render(request, 'pages/generate.html', context)

# GET 요청 vs POST 요청
# GET - html 파일을 주세요!!
# (주소창에 모든 흔적이 남음)
# POST - 어떠한 일을 처리해 주세요!!
#        새로운 글을 써주세요! 글을 삭제해주세요!
# (주소창에 흔적이 남지 않음 - ex. password 등)

def article_new(request):
    return render(request, 'pages/article_new.html')

def article_create(request):
    # request.POST => {'title' : '제목입니다', 'content' : '내용입니다'}
    title = request.POST.get('title')        # => '제목입니다'
    content = request.POST.get('content')    # => '내용입니다'

    context = {
        'title' : title,
        'content' : content,
    }
    return render(request, 'pages/article_create.html', context)

# Static Files
# Image, CSS, HTML 통틀어 이야기하는 자원 or 파일
# html 단독 -> 파일과 같은 폴더에 넣고, 상대 경로
# {% load static %}
def static_example(request):

    return render(request, 'pages/static_example.html')