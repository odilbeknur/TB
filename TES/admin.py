from django.contrib import admin
from .models import Category, User, Plants, Employer, Commission, Exam, UserRole, Files, CommissionType, Score


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(User)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Plants)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Employer)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'level', 'position', 'pos_duration', 'enter', 'plant']


@admin.register(Commission)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'lvl', 'group']


@admin.register(Exam)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'date']


@admin.register(UserRole)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Files)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'files', 'commission']


@admin.register(CommissionType)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Score)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'score']
