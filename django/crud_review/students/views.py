from django.shortcuts import render, redirect
from .models import Student

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
       
    context = {
        'student' : student,
    }
    return render(request, 'students/detail.html', context)

def delete(request, pk):
    if request.method = 'POST':
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

