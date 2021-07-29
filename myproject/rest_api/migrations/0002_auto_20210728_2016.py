# Generated by Django 3.2.5 on 2021-07-28 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='notes',
            field=models.CharField(blank=True, max_length=1500),
        ),
        migrations.AlterField(
            model_name='pet',
            name='animal_type',
            field=models.CharField(choices=[('DG', 'Dog'), ('CT', 'Cat'), ('HR', 'Horse')], max_length=2),
        ),
    ]
