# Generated by Django 5.0.3 on 2024-03-14 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0003_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
    ]