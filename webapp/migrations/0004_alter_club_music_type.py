# Generated by Django 4.2.6 on 2023-12-02 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_remove_club_contact_number_club_music_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='music_type',
            field=models.CharField(max_length=200),
        ),
    ]
