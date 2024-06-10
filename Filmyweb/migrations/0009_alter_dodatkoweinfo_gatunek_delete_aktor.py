# Generated by Django 4.0.3 on 2024-06-04 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Filmyweb', '0008_alter_dodatkoweinfo_gatunek_aktor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Inne'), (1, 'Komedia'), (2, 'Akcja'), (3, 'Sci-fi'), (4, 'Horror'), (5, 'Drama')], default=0),
        ),
        migrations.DeleteModel(
            name='Aktor',
        ),
    ]
