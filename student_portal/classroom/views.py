from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from classroom.models import Category, Course

from classroom.forms import NewCourseForm

def index(request):
    user = request.user
    courses = Course.objects.filter(enrolled = user)

    context = {
        'courses': courses,
    }
    return render(request, 'index.html', context)

def Categories(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    return render(request, 'classroom/categories.html', context )

def CategoryCourses(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    courses = Course.objects.filter(category=category)

    context = {
        'courses': courses,
        'category': category,
    }
    return render(request, 'classroom/categorycourse.html', context)

def newCourse(request):
    user = request.user
    if request.method == 'POST':
        form = NewCourseForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.cleaned_data.get('picture')
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            category = form.cleaned_data.get('category')
            syllabus = form.cleaned_data.get('syllabus')
            Course.objects.create(picture=picture, title=title, description=description, category=category, syllabus=syllabus, user=user)
            return redirect('my-courses')
    else:
        form = NewCourseForm
    context = {
        'form': form,
    }
    return render(request, 'classroom/newcourse.html', context)

@login_required
def enroll(request, course_id):
    user = request.user
    course = get_object_or_404(Course, id=course_id)
    course.enrolled.add(user)
    return redirect('index')    

@login_required
def deleteCourse(request, course_id):
    user = request.user
    course = get_object_or_404(Course, id=course_id)

    if user != course.user:
        return HttpResponseForbidden()
    else:
        course.delete()
    return redirect('my-courses')

@login_required
def editCourse(request, course_id):
    user = request.user
    course = get_object_or_404(Course, id=course_id)

    if user != course.user:
        return HttpResponseForbidden()
    else:
        if request.method == 'POST':
            form = NewCourseForm(request.POST, request.FILES, instance=course)
            if form.is_valid():
                course.picture = form.cleaned_data.get('picture')
                course.title = form.cleaned_data.get('title')
                course.description = form.cleaned_data.get('description')
                course.category = form.cleaned_data.get('category')
                course.syllabus = form.cleaned_data.get('syllabus')
                course.save()
                return redirect('my-courses')
        else:
            form = NewCourseForm(instance=course)
    context = {
        'form': form,
        'course': course,
    }
    return render(request, 'classroom/editcourse.html', context)

def myCourses(request):
    user = request.user
    courses = Course.objects.filter(user=user)

    context = {
        'courses': courses,
    }
    return render(request, 'classroom/mycourses.html', context)