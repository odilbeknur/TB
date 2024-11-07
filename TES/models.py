from django.db import models
from django.urls import reverse


# Create your models here.
STATUSES = (
        (u'pass', u'Прошел'),
        (u'fail', u'Не прошел'),
        (u'process', u'В процессе'),
    )

EXAMS = (
        (u'secure', u'Техника безопасности'),
        (u'fire', u'Пожарная безопасность'),
        (u'med', u'Медицинский контроль'),
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


class Files(models.Model):
    files = models.FileField(upload_to="files/", null=True, verbose_name='Файл')

    def __str__(self):
        return self.files.name if self.files else "No file"

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


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




class CommissionType(models.Model):
    title = models.CharField(max_length=255, verbose_name='Тип комиссии')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип комиссии'
        verbose_name_plural = 'Типы комиссий'

class Employee(models.Model):
        employee_num = models.CharField(max_length=10, blank=True, verbose_name="Регистрационный номер")
        name = models.CharField(max_length=255, unique=True, verbose_name='ФИО')
        image = models.ImageField(upload_to='images/', null=True, default='/images/emp_def.webp', verbose_name="Фото")
        level = models.IntegerField(verbose_name='Разряд', blank=True, null=True)
        department = models.TextField(choices=DEPARTMENT, max_length=255, blank=True, null=True, verbose_name='Должность')
        position = models.TextField(choices=POSITIONS, max_length=255, blank=True, null=True, verbose_name='Должность')
        enter = models.CharField(max_length=255, verbose_name='Период работы(с)', blank=True, null=True)
        pos_duration = models.IntegerField(verbose_name='Длительность на должности', blank=True, null=True)
        gender = models.CharField(max_length=10, blank=True, verbose_name="Пол")
        birth_date = models.DateField(blank=True, null=True, verbose_name="День рождения")
        region = models.CharField(max_length=255, blank=True, verbose_name="Место рождения")
        plant = models.ForeignKey(Plants, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Станция')

        def get_absolute_url(self):
            return reverse('employer_detail', kwargs={'pk': self.pk})

        def __str__(self):
            return self.name

        def get_image(self):
            pass

        class Meta:
            verbose_name = 'Сотрудник'
            verbose_name_plural = 'Сотрудники'
    


class Commission(models.Model):
        name = models.CharField(max_length=255, verbose_name='Название', blank=True, null=True,)
        leader = models.CharField(max_length=255, verbose_name='Председатель комиссии', blank=True, null=True,)
        image = models.ImageField(upload_to='images/', blank=True, null=True, default='/media/images/emp_def.webp', verbose_name='Протокол комиссии')
        lvl = models.CharField(max_length=255, verbose_name='Уровень комиссии')
        group = models.CharField(max_length=120, verbose_name='Номер группы')
        commission_type = models.ForeignKey(CommissionType, on_delete=models.CASCADE, blank=True, null=True,
                                            verbose_name='Тип комиссии')
        files = models.ForeignKey(Files, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Файл')
        members = models.ManyToManyField(Employee, verbose_name='Члены комиссии', related_name='member_commissions', blank=True)

        def __str__(self):
            return f'{self.name} - {self.leader}'

        def get_image(self):
            pass

        class Meta:
            verbose_name = 'Комиссия'
            verbose_name_plural = 'Комиссии'    
        

class Exam(models.Model):
    name = models.CharField(max_length=255, verbose_name='Тип экзамена')
    types = models.CharField(choices=EXAMS, max_length=255, blank=True, null=True)
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Комиссия')
    plant = models.ForeignKey(Plants, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Станция')
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.types

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'



class Score(models.Model):
    name = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, verbose_name='ФИО')
    score = models.FloatField(default=0)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Тип экзамена', related_name='экзамен')
    status = models.CharField(choices=STATUSES, max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'



