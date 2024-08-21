from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(User)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Plants)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


@admin.register(Employer)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image','level', 'department', 'position', 'pos_duration', 'enter', 'plant', 'exam', 'commission']


@admin.register(Commission)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'leader','image', 'files','lvl', 'group', 'description']


@admin.register(Exam)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'start', 'end', 'plant']


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