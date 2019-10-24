from django.shortcuts import render
import random

# Create your views here.
# 플라스크는 함수 인자가 없어도 됬는데
# 장고에서는 request를 첫 번째 파라미터로 받음
def index(request):

    context = {
        'name' : 'nwith',
    }       # 변수명은 크게 상관 없음, 튜플 형태만 지켜지면!

    return render(request, 'index.html', context)    # render함수를 사용해 html로 보여줌

# Template Variable
def dinner(request):
    foods = ['초밥', '카레', '칼국수', '치킨', '김치찌개']
    pick = random.choice(foods)
    context = {
        'pick' : pick,
    }
    return render(request, 'dinner.html', context)

# Variable Routing
def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'hello.html', context)

# 실습
# 1. '이름'과 '나이'를 Variable Routing'을 통해 받아서 자기소개
def introduce(request, name, age):
    context = {
        'name' : name,
        'age' : age,
    }
    return render(request, 'introduce.html', context)

# 2. 숫자 2개를 Variable Routing을 통해 받아 곱셈 결과 보여주기
def multiple(request, num1, num2):
    result = num1 * num2  # context 내부에서 실행해도 됨
    context = {
        'num1' : num1,
        'num2' : num2,
        'result' : result, # 'result' : num1 * num2
    }
    return render(request, 'multiple.html', context)

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
    return render(request, 'dtl.html', context)

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
    return render(request, 'birthday.html', context)
