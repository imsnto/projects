from django.urls import path, include

from classroom.views import Categories, newCourse, CategoryCourses, enroll, deleteCourse, newCourse, editCourse, myCourses
urlpatterns = [
    path('newcourse/', newCourse, name='newcourse'),
    path('mycourses/', myCourses, name='my-courses'),
    path('categories/', Categories, name='categories'),
    path('categories/<category_slug>', CategoryCourses, name='category-courses'),
    path('<course_id>/enroll', enroll, name='enroll'),
    path('<course_id>/edit', editCourse, name='edit-course'),
    path('<course-id/delete', deleteCourse, name='delete-course'),

]
