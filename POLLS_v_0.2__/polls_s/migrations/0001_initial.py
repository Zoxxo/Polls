# Generated by Django 3.1.6 on 2021-02-12 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('poll_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('question_type', models.CharField(max_length=200)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='polls_s.poll')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='polls_s.question')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('choice_text', models.CharField(max_length=200, null=True)),
                ('choice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choice', to='polls_s.choice')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poll', to='polls_s.poll')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='polls_s.question')),
            ],
        ),
    ]