# Generated by Django 3.0.3 on 2020-05-13 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20200513_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='netsalary',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
