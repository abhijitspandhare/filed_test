# Generated by Django 3.1.7 on 2021-04-01 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audiobook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('narrator', models.CharField(max_length=100)),
                ('duration', models.PositiveIntegerField(help_text='in seconds')),
                ('uploaded_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('duration', models.PositiveIntegerField(help_text='in seconds')),
                ('uploaded_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('duration', models.PositiveIntegerField(help_text='in seconds')),
                ('uploaded_time', models.DateTimeField(auto_now_add=True)),
                ('host', models.CharField(max_length=100)),
                ('participants', models.ManyToManyField(related_name='_podcast_participants_+', to='audioapi.Podcast')),
            ],
        ),
    ]
