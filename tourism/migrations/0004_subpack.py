# Generated by Django 3.2.12 on 2024-01-05 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0003_auto_20240103_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subpack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=50)),
                ('day', models.CharField(max_length=20)),
                ('night', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=255)),
                ('destination1', models.CharField(max_length=20)),
                ('destination2', models.CharField(max_length=20)),
                ('destination3', models.CharField(max_length=20)),
                ('destination_1', models.CharField(max_length=25)),
                ('destination_2', models.CharField(max_length=25)),
                ('destination_3', models.CharField(max_length=25)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('image1', models.ImageField(upload_to='uploads/')),
                ('image2', models.ImageField(upload_to='uploads/')),
                ('image3', models.ImageField(upload_to='uploads/')),
                ('pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourism.subpackage')),
            ],
        ),
    ]
