# Generated by Django 4.0.1 on 2022-02-15 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_alter_categoria_imagen_referencial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='imagen_referencial',
            field=models.ImageField(upload_to='aplicaciones/myblog/media/img/categorias/'),
        ),
    ]
