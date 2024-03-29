# Generated by Django 2.2.9 on 2020-11-01 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('body', models.TextField(verbose_name='Содержание статьи')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
                ('active', models.BooleanField(default=True, verbose_name='Активность')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post', verbose_name='Пост')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
