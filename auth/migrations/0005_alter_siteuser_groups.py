# Generated by Django 4.0.7 on 2022-11-15 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('custom_auth', '0004_alter_siteuser_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
    ]
