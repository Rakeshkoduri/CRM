# Generated by Django 4.1.2 on 2022-12-15 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_customer_profile_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='profile_pic',
            new_name='image',
        ),
    ]
