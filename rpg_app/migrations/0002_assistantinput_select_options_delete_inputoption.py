# Generated by Django 4.1.7 on 2023-02-23 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpg_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assistantinput',
            name='select_options',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.DeleteModel(
            name='InputOption',
        ),
    ]