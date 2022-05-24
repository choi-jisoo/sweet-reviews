# Generated by Django 2.2.5 on 2022-05-24 06:09

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('bio', models.TextField(blank=True, default='', null=True)),
                ('preference', models.CharField(blank=True, choices=[('books', 'Books'), ('movies', 'Movies')], max_length=6, null=True)),
                ('language', models.CharField(blank=True, choices=[('en', 'English'), ('kr', 'Korean')], max_length=2, null=True)),
                ('favourite_book_genre', models.CharField(blank=True, choices=[('adventrue', 'Adventure'), ('classics', 'Classics'), ('crime', 'Crime'), ('fantasy', 'Fantasy'), ('horror', 'Horror'), ('mystery', 'Mystery'), ('nonfiction', 'Nonfiction'), ('poetry', 'Poetry'), ('romance', 'Romance'), ('sci-fi', 'Sci-Fi')], max_length=20, null=True)),
                ('favourite_movie_genre', models.CharField(blank=True, choices=[('action', 'Action'), ('adventrue', 'Adventure'), ('biography', 'Biography'), ('comedy', 'Comedy'), ('drama', 'Drama'), ('fantasy', 'Fantasy'), ('history', 'History'), ('horror', 'Horror'), ('mystery', 'Mystery'), ('romance', 'Romance'), ('thriller', 'Thriller'), ('sci-fi', 'Sci-Fi'), ('war', 'War')], max_length=20, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]