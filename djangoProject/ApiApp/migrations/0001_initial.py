# Generated by Django 3.2.6 on 2021-08-19 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
