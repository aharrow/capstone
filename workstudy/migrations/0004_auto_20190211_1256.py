# Generated by Django 2.1.5 on 2019-02-11 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workstudy', '0003_auto_20190211_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='first_name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='student_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
