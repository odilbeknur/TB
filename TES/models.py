from django.db import models
from django.urls import reverse


# Create your models here.
STATUSES = (
        (u'pass', u'Прошел'),
        (u'fail', u'Не прошел'),
        (u'process', u'В процессе'),
    )

EXAMS = (
        (u'tb', u'Экзамен по ТБ'),
        (u'med', u'Экзамен по Медицине'),
        (u'fire', u'Экзамен по Пожарной безопасности'),
    )
POSITIONS = (
    (u'Начальник отдела', u'Начальник отдела'),
    (u'Главный специалист', u'Главный специалист'),
    (u'Ведущий специалист', u'Ведущий специалист'),
)

DEPARTMENT = (
    (u'Отдел управления проектами', u'Отдел управления проектами'),
    (u'Отдел технического обслуживания', u'Отдел технического обслуживания'),
    (u'Отдел исследования и разработки', u'Отдел исследования и разработки'),
)



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
    password = models.CharField(max_length=255, default='TES123456789', verbose_name='Пароль')

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
    name = models.CharField(max_length=255, verbose_name='Тип экзамена')
    type = models.CharField(choices=EXAMS, max_length=255, blank=True, null=True)
    plant = models.ForeignKey(Plants, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Станция')
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'



class CommissionType(models.Model):
    title = models.CharField(max_length=255, verbose_name='Тип комиссии')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип комиссии'
        verbose_name_plural = 'Типы комиссий'


class Files(models.Model):
    files = models.FileField(upload_to="files/", null=True, verbose_name='Файл')

    def __str__(self):
        return self.files.name if self.files else "No file"

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'



class Commission(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название', blank=True, null=True,)
    leader = models.CharField(max_length=255, verbose_name='Председатель комиссии', blank=True, null=True,)
    image = models.ImageField(upload_to='images/', blank=True, null=True, default='/media/images/emp_def.webp')
    lvl = models.CharField(max_length=255, verbose_name='Уровень комиссии')
    group = models.CharField(max_length=120, verbose_name='Номер группы')
    commission_type = models.ForeignKey(CommissionType, on_delete=models.CASCADE, blank=True, null=True,
                                        verbose_name='Тип комиссии')
    description = models.TextField(default='Описание', verbose_name='Описание')
    files = models.ForeignKey(Files, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Файл')

    def __str__(self):
        return self.lvl

    def get_image(self):
        pass

    class Meta:
        verbose_name = 'Комиссия'
        verbose_name_plural = 'Комиссии'


class Employer(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='ФИО')
    image = models.ImageField(upload_to='images/', null=True, default='/images/emp_def.webp')
    level = models.IntegerField(verbose_name='Разряд')
    department = models.TextField(choices=DEPARTMENT, max_length=255, blank=True, null=True, verbose_name='Должность')
    position = models.TextField(choices=POSITIONS, max_length=255, blank=True, null=True, verbose_name='Должность')
    pos_duration = models.IntegerField(verbose_name='Длительность на должности')
    enter = models.CharField(max_length=255, verbose_name='Период работы(с)')
    plant = models.ForeignKey(Plants, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Станция')
    description = models.TextField(default='Описание', verbose_name='Описание')
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Комиссия')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Тип экзамена')

    def get_absolute_url(self):
        return reverse('employer_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    def get_image(self):
        pass

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Score(models.Model):
    name = models.ForeignKey(Employer, on_delete=models.CASCADE, blank=True, null=True, verbose_name='ФИО')
    score = models.FloatField(default=0)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Тип экзамена', related_name='экзамен')
    status = models.CharField(choices=STATUSES, max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'


