# Generated by Django 3.1.1 on 2020-10-05 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('english_name', models.CharField(max_length=100)),
                ('scientific_name', models.CharField(max_length=100)),
                ('avg_weight', models.CharField(max_length=100, null=True)),
                ('avg_size', models.CharField(max_length=100, null=True)),
                ('distribution_area', models.CharField(max_length=100, null=True)),
                ('characteristics', models.TextField(blank=True)),
                ('image_1', models.ImageField(blank=True, upload_to='images')),
                ('image_2', models.ImageField(blank=True, upload_to='images')),
                ('image_3', models.ImageField(blank=True, upload_to='images')),
                ('image_4', models.ImageField(blank=True, upload_to='images')),
                ('image_5', models.ImageField(blank=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='AnimalImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_image', models.ImageField(blank=True, upload_to='')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.animal')),
                ('upload_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]