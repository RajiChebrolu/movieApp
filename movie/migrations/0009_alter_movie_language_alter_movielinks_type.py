# Generated by Django 5.0.2 on 2024-04-16 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_download_links_movie_cast_alter_movie_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(choices=[('english', 'ENGLISH'), ('korean', 'KOREAN'), ('hindi', 'HINDI'), ('spanish', 'SPANISh')], max_length=10),
        ),
        migrations.AlterField(
            model_name='movielinks',
            name='type',
            field=models.CharField(choices=[('D', 'Download Link'), ('W', 'Watch Link')], max_length=1),
        ),
    ]
