# Generated by Django 4.2.1 on 2023-05-31 14:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_alter_video_options_remove_video_course_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': 'Video', 'verbose_name_plural': 'Videos'},
        ),
        migrations.AddField(
            model_name='video',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='common.course'),
        ),
        migrations.AddField(
            model_name='video',
            name='file',
            field=models.FileField(default=1, upload_to='videos/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='video',
            table='Videos',
        ),
    ]