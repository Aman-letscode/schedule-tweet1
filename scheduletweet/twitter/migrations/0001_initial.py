# Generated by Django 3.1.2 on 2020-10-25 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterSchedulerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet', models.TextField(max_length=240)),
                ('tweet_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sent', models.BooleanField(default=False)),
            ],
        ),
    ]