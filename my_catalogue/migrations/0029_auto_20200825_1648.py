# Generated by Django 2.2.13 on 2020-08-25 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0028_auto_20200825_1642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name_fi',
            new_name='name_fil',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='description_fi',
            new_name='description_fil',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title_fi',
            new_name='title_fil',
        ),
    ]