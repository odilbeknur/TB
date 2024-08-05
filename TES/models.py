from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class UserRole(models.Model):
    title = models.CharField(max_length=255, verbose_name='Роль пользователя')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


class User(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя пользователя')
    role = models.ManyToManyField(UserRole, related_name='users', verbose_name='Роль')

    def get_image(self):
        pass

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Plants(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название станции')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.TextField(default='Описание', verbose_name='Описание')

    def __str__(self):
        return self.name

    def get_image(self):
        pass

    class Meta:
        verbose_name = 'Станция'
        verbose_name_plural = 'Станции'


class Exam(models.Model):
    type = models.CharField(max_length=255, verbose_name='Тип экзамена')
    date = models.DateField(default=None, blank=True, null=True, verbose_name='Дата')
    plant = models.ForeignKey(Plants, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Станция')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'


class CommissionType(models.Model):
    title = models.CharField(max_length=255, verbose_name='Тип каммиссии')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип камиссии'
        verbose_name_plural = 'Типы камиссий'


class Files(models.Model):
    files = models.FileField(upload_to="files/", null=True, verbose_name='Файл')

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


class Commission(models.Model):
    user_name = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    lvl = models.CharField(max_length=255, verbose_name='Уровень камиссии')
    group = models.CharField(max_length=120, verbose_name='Номер группы')
    commission_type = models.ForeignKey(CommissionType, on_delete=models.CASCADE, blank=True, null=True,
                                        verbose_name='Тип коммиссии')
    description = models.TextField(default='Описание', verbose_name='Описание')
    files = models.ForeignKey(Files, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Файл')

    def __str__(self):
        return self.user_name

    def get_image(self):
        pass

    class Meta:
        verbose_name = 'Камиссия'
        verbose_name_plural = 'Камиссии'


class Employer(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='ФИО')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    level = models.IntegerField(verbose_name='Разряд')
    position = models.TextField(max_length=255, verbose_name='Должность')
    pos_duration = models.IntegerField(verbose_name='Длительность на должности')
    enter = models.CharField(max_length=255, verbose_name='Период работы(с)')
    plant = models.ForeignKey(Plants, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Станция')
    description = models.TextField(default='Описание', verbose_name='Описание')
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Камиссия')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Тип экзамена')

    def get_absolute_url(self):
        return reverse('employer_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    def get_image(self):
        pass

    class Meta:
        verbose_name = 'Сатрудник'
        verbose_name_plural = 'Сатрудники'


class Score(models.Model):
    name = models.ForeignKey(Employer, on_delete=models.CASCADE, blank=True, null=True, verbose_name='ФИО')
    score = models.FloatField(default=0)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Тип экзамена', related_name='экзамен')

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'



