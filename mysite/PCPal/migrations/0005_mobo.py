# Generated by Django 2.0.7 on 2018-07-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PCPal', '0004_remove_cpu_cpu_cores'),
    ]

    operations = [
        migrations.CreateModel(
            name='MOBO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobo_name', models.CharField(max_length=200)),
                ('mobo_price', models.CharField(max_length=200)),
                ('mobo_ram', models.CharField(max_length=200)),
            ],
        ),
    ]