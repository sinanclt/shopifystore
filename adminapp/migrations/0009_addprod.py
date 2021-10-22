# Generated by Django 3.2.2 on 2021-09-30 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0008_bannerr'),
    ]

    operations = [
        migrations.CreateModel(
            name='addprod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('prod_name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=500)),
                ('price', models.CharField(max_length=30)),
                ('size_dresses', models.CharField(max_length=30)),
                ('size_footwears', models.CharField(max_length=30)),
                ('image', models.CharField(max_length=500)),
            ],
        ),
    ]