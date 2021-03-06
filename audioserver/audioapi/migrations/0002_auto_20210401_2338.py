# Generated by Django 3.1.7 on 2021-04-01 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audioapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='podcast',
            name='participants',
            field=models.ManyToManyField(blank=True, to='audioapi.Participants'),
        ),
    ]
