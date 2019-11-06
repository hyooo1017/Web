from django.shortcuts import render, redirect
from .models import Student, Comment

# Create your views here.
def index(request):
    students = Student.objects.all().order_by('-id')    # => Query Set ~= List

    context = {
        'students' : students,
    }
    return render(request, 'students/index.html', context)

def new(request):
    if request.method == 'POST':     # def create
        name = request.POST.get('name')
        age = request.POST.get('age')

        student = Student.objects.create(name = name, age = age)
        return redirect('students:detail', student.pk) 

    else:
        # new page를 보여주면 됨 (def new)
        return render(request, 'students/new.html')

# def create(request):
#     name = request.POST.get('name')
#     age = request.POST.get('age')

#     student = Student.objects.create(name = name, age = age)
#     return redirect('students:detail', student.pk) 

def detail(request, pk):
    student = Student.objects.get(pk=pk)
    comments = student.comment_set.all()

    context = {
        'student' : student,
        'comments' : comments,
    }
    return render(request, 'students/detail.html', context)

def delete(request, pk):
    if request.method == 'POST':
        student = Student.objects.get(pk=pk)
        student.delete()
        context = {
            'student' : student,
        }
        return redirect('students:index')

def edit(request, pk):
    student = Student.objects.get(pk=pk)

    if request.method == 'POST':        # def update
        name = request.POST.get('name')
        age = request.POST.get('age')
        
        student.name = name
        student.age = age
        student.save()

        context = {
            'student' : student,
        }
        return redirect('students:detail', student.pk)

    else:                               # def edit
        context = {
            'student' : student,
        }
        return render(request, 'students/edit.html', context)

# def update(request, pk):

#     student = Student.objects.get(pk=pk)

#     name = request.POST.get('name')
#     age = request.POST.get('age')
    
#     student.name = name
#     student.age = age
#     student.save()

#     context = {
#         'student' : student,
#     }
#     return redirect('students:detail', student.pk)     # detail 페이지로 redirect

# POST 요청을 받음 -> redirect
def comments_new(request, student_pk):
    # 1. request에서 데이터 가져오기
    content = request.POST.get('content')

    # 2. Comment 생성
    comment = Comment()
    comment.content = content
    comment.student_id = student_pk
    comment.save()
    
    # 3. student 상세 페이지로 redirect
    return redirect('students:detail', student_pk)

# POST 요청을 받음
def comments_delete(request, student_pk, pk):
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    return redirect('students:detail', student_pk)


def comments_edit(request, student_pk, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'POST':
        # POST
        # 1. POST로 넘어온 데이터 가져오기
        content = request.POST.get('content')

        # 2. comment에 바꿔 넣기 & 저장
        comment.content = content
        comment.save()

        # 3. student 상세 페이지로 redirect
        return redirect('students:detail', student_pk)
    else:
        # GET
        context = {
            'comment': comment,
        }
        return render(request, 'students/comments_edit.html', context)