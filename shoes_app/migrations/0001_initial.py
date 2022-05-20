# Generated by Django 4.0.4 on 2022-05-17 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=25)),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('brand', models.CharField(max_length=20)),
                ('release_date', models.DateField()),
                ('retail_price', models.FloatField()),
                ('goat_price', models.FloatField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100)),
                ('parent_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shoes_app.item')),
                ('parent_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shoes_app.title')),
            ],
        ),
    ]