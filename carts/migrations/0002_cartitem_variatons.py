# Generated by Django 3.2.8 on 2021-10-10 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_variation'),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variatons',
            field=models.ManyToManyField(blank=True, to='store.Variation'),
        ),
    ]
