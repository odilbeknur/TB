# Generated by Django 5.0.7 on 2024-08-02 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TES', '0015_employer_commission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='ФИО'),
        ),
    ]