# Generated by Django 4.1.2 on 2022-10-24 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_options'),
        ('rooms', '0002_alter_amenity_options_alter_room_kind'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='amenities',
            field=models.ManyToManyField(to='rooms.amenity'),
        ),
        migrations.AddField(
            model_name='room',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.category'),
        ),
    ]
