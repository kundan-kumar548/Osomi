# Generated by Django 2.1.4 on 2019-01-06 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistaccount',
            name='specialist_In',
            field=models.CharField(choices=[('Painters', 'Painters'), ('Home decorators', 'Home decorators'), ('Beauty & SPAs', 'Beauty & SPAs'), ('Other small business', 'Other small business')], default='Painters', max_length=50),
        ),
    ]
