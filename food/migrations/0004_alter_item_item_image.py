# Generated by Django 4.0 on 2024-01-25 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_alter_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.ImageField(default='Food/None/seample.jpg', upload_to='Food'),
        ),
    ]