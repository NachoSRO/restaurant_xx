# Generated by Django 3.1.2 on 2020-11-04 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_mesa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mesa',
            name='cliente',
        ),
        migrations.CreateModel(
            name='Mesa_Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.mesa')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
            ],
            options={
                'db_table': 'Mesa_Cliente',
            },
        ),
    ]
