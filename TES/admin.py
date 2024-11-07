from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(User)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Plants)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


@admin.register(Employee)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','employee_num', 'name', 'image','level', 'department', 'position', 'enter', 'pos_duration','gender', 'birth_date', 'region','plant']


@admin.register(Commission)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'leader','image', 'files','lvl', 'group']


@admin.register(Exam)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'types', 'start', 'end', 'plant', 'commission']


@admin.register(UserRole)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Files)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'files']


@admin.register(CommissionType)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Score)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'score', 'exam', 'status']

# @admin.register(Events)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'start', 'end']