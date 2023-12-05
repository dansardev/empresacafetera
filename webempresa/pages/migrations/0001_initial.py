# Generated by Django 4.2.7 on 2023-11-28 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('slug', models.CharField(max_length=150, unique=True, verbose_name='URL amigable')),
                ('order', models.SmallIntegerField(default=0, verbose_name='Orden')),
                ('visible', models.BooleanField(default=True, verbose_name='¿Visible?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Página',
                'verbose_name_plural': 'Páginas',
                'ordering': ['order', 'title'],
            },
        ),
    ]