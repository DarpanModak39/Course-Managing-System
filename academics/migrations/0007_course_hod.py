# Generated by Django 4.0 on 2022-01-21 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0006_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='hod',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
