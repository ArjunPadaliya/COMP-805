# Generated by Django 2.0.1 on 2018-02-10 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20180210_0202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=256, null=True)),
                ('location', models.CharField(max_length=64, null=True)),
                ('degree', models.CharField(max_length=64, null=True)),
                ('major', models.CharField(max_length=64, null=True)),
                ('gpa', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='experience',
            name='location',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
