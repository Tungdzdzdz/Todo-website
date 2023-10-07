# Generated by Django 4.2.4 on 2023-10-05 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('description', models.TextField(max_length=1000)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['completed'],
            },
        ),
    ]