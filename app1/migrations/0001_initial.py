# Generated by Django 3.0.3 on 2020-05-06 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.CharField(max_length=10, unique=True)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('picture', models.ImageField(null=True, upload_to='')),
                ('address', models.CharField(blank=True, max_length=255)),
                ('p_address', models.CharField(blank=True, max_length=255)),
                ('dob', models.DateTimeField()),
                ('post', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('doj', models.DateTimeField(null=True)),
                ('W_email', models.EmailField(max_length=50)),
                ('w_phone', models.CharField(max_length=30)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Department')),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Designation')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Gender')),
                ('mstatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.MaritalStatus')),
            ],
        ),
    ]
