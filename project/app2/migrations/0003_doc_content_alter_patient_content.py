# Generated by Django 4.0.4 on 2022-04-24 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='content',
            field=models.TextField(default=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='content',
            field=models.TextField(default=True),
        ),
    ]
