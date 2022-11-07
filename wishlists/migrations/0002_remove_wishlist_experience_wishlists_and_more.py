# Generated by Django 4.1.2 on 2022-11-06 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_room_name_alter_amenity_description_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('experiences', '0003_alter_experience_category_alter_experience_host_and_more'),
        ('wishlists', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='experience_wishlists',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='room_wishlists',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='experiences',
            field=models.ManyToManyField(related_name='wishlists', to='experiences.experience'),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='rooms',
            field=models.ManyToManyField(related_name='wishlists', to='rooms.room'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlists', to=settings.AUTH_USER_MODEL),
        ),
    ]
