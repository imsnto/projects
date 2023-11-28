from django.contrib import admin

from classroom.forms import NewCourseForm
from classroom.models import Category, Course


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title', )}

admin.site.register(Course)
admin.site.register(Category, CategoryAdmin)