# Generated by Django 3.2.9 on 2021-12-01 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectblog',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projectblog',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
