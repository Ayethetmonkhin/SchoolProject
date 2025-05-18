from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *
# Create your views here.
def indexView (request):
    return render(request, 'index.html')

def courseView(request):
    courses = Course.objects.all()
    return render(request,'courses.html', {'courses':courses})

def trainerView(request):
    return render(request,'trainers.html')

def aboutView(request):
    return render(request,'about.html')

def contactView(request):
    return render(request, 'contact.html')

def eventView(request):
    return render(request,'events.html')

# add course nae courses plus
def addCourse(request):
    course = CourseModelForm()
    if request.method == "POST":
        course = CourseModelForm(request.POST, request.FILES)
        if course.is_valid():
            course.save()
            return redirect('/course/')
        else:
            return HttpResponse('Error')
    else:
        course = CourseModelForm()
        return render(request, 'addcourse.html', {'course':course})

#   add teacher nae trainer ko plus 
def addTeacher(request):
    teacher = TeacherModelForm()
    if request.method == "POST":
        teacher = TeacherModelForm(request.POST, request.FILES)
        if teacher.is_valid():
            teacher.save()
            return redirect('/trainer/')
        else:
            return HttpResponse('Error')
    else:
        return render (request, 'addTeacher.html',{'teacher':teacher})
    
# updatecourse ko yy
def updateCourse(request, pk):
    course_obj = Course.objects.get(id=pk)
    fm = UpdateCourseFm()
    if request.method == 'POST':
        photo = request.FILES['photo_fm']
        name = request.POST.get('name_fm')
        desc = request.POST.get('desc_fm')
        fee = request.POST.get('fee_fm')
        course = Course.objects.filter(id=pk)
        course.update(photo=photo, name=name, fee=fee, description =desc)
        return redirect('/index/')
    else:
        return render(request, 'updatecourse.html', {'course_obj':course_obj,'fm':fm})

