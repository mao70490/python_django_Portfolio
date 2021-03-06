# Generated by Django 3.2.7 on 2021-11-14 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.IntegerField(default=0)),
                ('shipping', models.IntegerField(default=0)),
                ('grandtotal', models.IntegerField(default=0)),
                ('customname', models.CharField(default='', max_length=100)),
                ('customemail', models.CharField(default='', max_length=100)),
                ('customadr', models.CharField(default='', max_length=100)),
                ('paytype', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(default='', max_length=100)),
                ('pprice', models.IntegerField(default=0)),
                ('pimages', models.CharField(default='', max_length=100)),
                ('pdescription', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='DetailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(default='', max_length=100)),
                ('unitprice', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('dtotal', models.IntegerField(default=0)),
                ('dorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartapp.ordermodel')),
            ],
        ),
    ]
