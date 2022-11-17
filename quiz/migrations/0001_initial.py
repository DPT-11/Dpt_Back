# Generated by Django 4.0.4 on 2022-11-18 03:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('answer', models.CharField(max_length=20)),
                ('correct', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Cookie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cookie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.cookie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30)),
                ('answer1', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='answer1', to='quiz.answer')),
                ('answer2', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='answer2', to='quiz.answer')),
                ('answer3', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='answer3', to='quiz.answer')),
                ('answer4', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='answer4', to='quiz.answer')),
                ('answer5', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='answer5', to='quiz.answer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cookie',
            name='questions',
            field=models.ManyToManyField(to='quiz.question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
