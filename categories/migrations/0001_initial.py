# Generated by Django 4.1.2 on 2022-10-24 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('kind', models.CharField(choices=[('room', 'Room'), ('experience', 'Experience')], max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
