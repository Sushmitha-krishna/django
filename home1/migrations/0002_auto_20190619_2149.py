# Generated by Django 2.2.2 on 2019-06-20 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='total_book_written',
            field=models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')], max_length=1),
        ),
    ]
