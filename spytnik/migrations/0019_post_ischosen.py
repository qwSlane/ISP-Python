# Generated by Django 4.0.4 on 2022-06-01 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spytnik', '0018_delete_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='isChosen',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
