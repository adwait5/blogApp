# Generated by Django 3.0.1 on 2020-02-23 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='stream',
            field=models.CharField(default='python', max_length=100),
        ),
    ]
