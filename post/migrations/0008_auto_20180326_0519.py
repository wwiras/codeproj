# Generated by Django 2.0.3 on 2018-03-25 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20180326_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_exp',
            field=models.DateTimeField(verbose_name='Expiry Date'),
        ),
    ]