# Generated by Django 5.0.2 on 2024-04-05 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_alter_movie_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_image',
            field=models.ImageField(blank=True, null=True, upload_to='movies/'),
        ),
    ]
