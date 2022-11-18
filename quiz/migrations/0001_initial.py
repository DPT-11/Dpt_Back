# Generated by Django 4.0.4 on 2022-11-18 21:13

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
            name='NewAnswer',
            fields=[
                ('answer1', models.CharField(max_length=20)),
                ('option1_1', models.CharField(max_length=20)),
                ('option1_2', models.CharField(blank=True, max_length=20, null=True)),
                ('option1_3', models.CharField(blank=True, max_length=20, null=True)),
                ('option1_4', models.CharField(blank=True, max_length=20, null=True)),
                ('answer2', models.CharField(max_length=20)),
                ('option2_1', models.CharField(max_length=20)),
                ('option2_2', models.CharField(blank=True, max_length=20, null=True)),
                ('option2_3', models.CharField(blank=True, max_length=20, null=True)),
                ('option2_4', models.CharField(blank=True, max_length=20, null=True)),
                ('answer3', models.CharField(max_length=20)),
                ('option3_1', models.CharField(max_length=20)),
                ('option3_2', models.CharField(blank=True, max_length=20, null=True)),
                ('option3_3', models.CharField(blank=True, max_length=20, null=True)),
                ('option3_4', models.CharField(blank=True, max_length=20, null=True)),
                ('answer4', models.CharField(max_length=20)),
                ('option4_1', models.CharField(max_length=20)),
                ('option4_2', models.CharField(blank=True, max_length=20, null=True)),
                ('option4_3', models.CharField(blank=True, max_length=20, null=True)),
                ('option4_4', models.CharField(blank=True, max_length=20, null=True)),
                ('answer5', models.CharField(max_length=20)),
                ('option5_1', models.CharField(max_length=20)),
                ('option5_2', models.CharField(blank=True, max_length=20, null=True)),
                ('option5_3', models.CharField(blank=True, max_length=20, null=True)),
                ('option5_4', models.CharField(blank=True, max_length=20, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question1', to='quiz.question')),
                ('question2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question2', to='quiz.question')),
                ('question3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question3', to='quiz.question')),
                ('question4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question4', to='quiz.question')),
                ('question5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question5', to='quiz.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
                ('score', models.IntegerField(blank=True, default=0, null=True)),
                ('answer1', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='guestanswer1', to='quiz.newanswer')),
                ('answer2', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='guestanswer2', to='quiz.newanswer')),
                ('answer3', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='guestanswer3', to='quiz.newanswer')),
                ('answer4', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='guestanswer4', to='quiz.newanswer')),
                ('answer5', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='guestanswer5', to='quiz.newanswer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['score', 'nickname'],
            },
        ),
        migrations.AddField(
            model_name='cookie',
            name='questions',
            field=models.ManyToManyField(to='quiz.question'),
        ),
    ]
