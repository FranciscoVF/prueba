# Generated by Django 3.1.1 on 2020-10-02 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0002_auto_20201002_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelobase',
            name='hora_actualizado',
            field=models.DateTimeField(),
        ),
    ]