# Generated by Django 4.0.2 on 2022-06-24 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0007_alter_livro_disciplina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='imagem',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
