# Generated by Django 5.0.3 on 2024-03-29 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playername', models.CharField(max_length=30)),
                ('playersurname', models.CharField(max_length=35)),
                ('playerage', models.CharField(max_length=5)),
                ('playerspeciality', models.CharField(max_length=20)),
            ],
        ),
    ]
