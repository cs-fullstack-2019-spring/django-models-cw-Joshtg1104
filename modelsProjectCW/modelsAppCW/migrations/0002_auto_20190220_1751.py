# Generated by Django 2.2 on 2019-02-20 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelsAppCW', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='color',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='dog',
            name='gender',
            field=models.CharField(max_length=7),
        ),
        migrations.DeleteModel(
            name='Color',
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
    ]