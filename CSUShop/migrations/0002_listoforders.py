# Generated by Django 4.0.5 on 2022-06-11 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSUShop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListofOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('idnum', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('progyear', models.CharField(max_length=50)),
            ],
        ),
    ]
