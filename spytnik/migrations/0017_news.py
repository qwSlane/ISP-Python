# Generated by Django 4.0.4 on 2022-05-28 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spytnik', '0016_alter_vote_voted_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('published_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]