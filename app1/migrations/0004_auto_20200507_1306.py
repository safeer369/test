# Generated by Django 3.0.3 on 2020-05-07 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20200507_1259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='p_address',
            new_name='paddress',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='W_email',
            new_name='wemail',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='w_phone',
            new_name='wphone',
        ),
    ]