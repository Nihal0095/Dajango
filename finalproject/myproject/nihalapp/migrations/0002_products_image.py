# Generated by Django 5.0.3 on 2024-05-07 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nihalapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(default=2, upload_to='media'),
            preserve_default=False,
        ),
    ]
