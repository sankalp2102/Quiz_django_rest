# Generated by Django 4.2.6 on 2024-02-04 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=150)),
                ('answer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='correct_answer', to='quiz.answer')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quiz.category')),
                ('choices', models.ManyToManyField(related_name='choices', to='quiz.answer')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_name', models.CharField(max_length=150)),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quiz.category')),
                ('question', models.ManyToManyField(blank=True, to='quiz.question')),
            ],
            options={
                'verbose_name_plural': 'Quizes',
            },
        ),
    ]
