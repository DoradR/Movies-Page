# Generated by Django 4.0.3 on 2022-03-14 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Filmyweb', '0004_film_imdb_ratting_film_plakat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='imdb_ratting',
            new_name='imdb_rating',
        ),
    ]
