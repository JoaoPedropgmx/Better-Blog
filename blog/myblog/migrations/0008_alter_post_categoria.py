# Generated by Django 4.2.4 on 2023-08-30 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0007_categoria_post_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categoria',
            field=models.CharField(default='Nenhuma', max_length=255),
        ),
    ]
