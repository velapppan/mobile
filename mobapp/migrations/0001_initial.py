# Generated by Django 4.1 on 2022-08-25 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('band', models.CharField(max_length=50)),
                ('display', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
                ('rating', models.FloatField(default=3, null=True)),
            ],
        ),
    ]