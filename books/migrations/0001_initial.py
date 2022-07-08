# Generated by Django 2.2.5 on 2022-07-08 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('year', models.IntegerField()),
                ('cover_image', models.ImageField(upload_to='')),
                ('rating', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='categories.Category')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='people.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
