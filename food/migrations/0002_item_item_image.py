# Generated by Django 4.0 on 2024-01-25 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.google.fr/search?q=placeholder+image&tbm=isch&ved=2ahUKEwjuouCPsvmDAxWLXqQEHU0OABcQ2-cCegQIABAA&oq=placeholder+&gs_lcp=CgNpbWcQARgBMgQIIxAnMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgYIABAHEB46BAgAEB46BggAEAUQHlD1BljXEGCVH2gAcAB4AYABqwOIAbIQkgEJMC4yLjQuMS4xmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=RsayZe7nOYu9kdUPzZyAuAE&bih=668&biw=1469#imgrc=vJkCGU5orcVcLM', max_length=500),
        ),
    ]
