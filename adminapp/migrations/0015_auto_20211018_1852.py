# Generated by Django 3.2.2 on 2021-10-18 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0014_auto_20211018_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='addprod',
            name='discount',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='prod_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=300)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.category')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.addprod')),
            ],
        ),
    ]
