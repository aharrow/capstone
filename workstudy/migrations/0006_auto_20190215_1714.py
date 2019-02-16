# Generated by Django 2.1.5 on 2019-02-15 22:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('workstudy', '0005_auto_20190213_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='sitePlacementRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('after_school', models.IntegerField(null=True)),
                ('medical', models.IntegerField(null=True)),
                ('community_center', models.IntegerField(null=True)),
                ('charity_org', models.IntegerField(null=True)),
                ('hospice', models.IntegerField(null=True)),
                ('other', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='siteinfo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='studentplacement',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='studentschedule',
            name='personal_info',
        ),
        migrations.RemoveField(
            model_name='studentschedule',
            name='semester',
        ),
        migrations.AddField(
            model_name='appdata',
            name='car',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='appdata',
            name='carpool',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='appdata',
            name='ccec_ws',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='appdata',
            name='clearances',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='appdata',
            name='foreign_lang',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='appdata',
            name='grad_month',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='appdata',
            name='grad_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='appdata',
            name='hear_about_ccec',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='appdata',
            name='keep_schedule',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='appdata',
            name='languages',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='appdata',
            name='major',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='appdata',
            name='phone_num',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='appdata',
            name='placement',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='appdata',
            name='previous_site',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='appdata',
            name='prior_work',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='appdata',
            name='remain_at_site',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='appdata',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appdata',
            name='wanted_hours',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='appdata',
            name='work_study',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='siteinfo',
            name='comments',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='siteinfo',
            name='second_contact_number',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='studentplacement',
            name='app_data',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workstudy.AppData'),
        ),
        migrations.AddField(
            model_name='studentplacement',
            name='child_abuse',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='studentplacement',
            name='comments',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='studentplacement',
            name='driver',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='studentplacement',
            name='fbi_fingerprint',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='studentplacement',
            name='physical',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='studentplacement',
            name='ppd',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='studentplacement',
            name='state_police',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='studentplacement',
            name='total_hours',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='studentschedule',
            name='day',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='studentschedule',
            name='end_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='studentschedule',
            name='start_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='studentschedule',
            name='student_placement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workstudy.StudentPlacement'),
        ),
        migrations.AlterField(
            model_name='appavailability',
            name='day',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='appavailability',
            name='end_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='appavailability',
            name='start_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='siteavailability',
            name='day',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='siteavailability',
            name='end_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='siteavailability',
            name='start_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='address',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='description',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='second_contact',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='second_contact_email',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='site_name',
            field=models.CharField(max_length=256, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='supervisor',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='supervisor_email',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='supervisor_phone',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='siteplacementrank',
            name='app_data',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workstudy.AppData'),
        ),
    ]