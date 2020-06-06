# Generated by Django 3.0.7 on 2020-06-06 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=250, unique=True, verbose_name='adresse_email')),
                ('profile_image', models.ImageField(blank=True, upload_to='profile_pics/')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('reports', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
