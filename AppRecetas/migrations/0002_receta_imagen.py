# Generated by Django 4.1.7 on 2023-05-10 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppRecetas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]
