# Generated by Django 4.1 on 2022-10-26 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_actor'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actores',
            field=models.ManyToManyField(to='movie.actor'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='edad',
            field=models.IntegerField(),
        ),
    ]
