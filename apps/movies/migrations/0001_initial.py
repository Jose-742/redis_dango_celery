# Generated by Django 4.2.5 on 2023-09-27 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('sobrenome', models.CharField(max_length=80)),
                ('idade', models.IntegerField()),
                ('linguagem', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'programadores',
            },
        ),
    ]