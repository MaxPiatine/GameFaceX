# Generated by Django 4.0.4 on 2022-11-05 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('x', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=255)),
                ('socials', models.CharField(max_length=64)),
                ('stream', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('followers', models.IntegerField(blank=True, default=None, max_length=16, null=True)),
                ('details', models.CharField(max_length=255)),
                ('traffic', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='quota',
            name='services',
            field=models.CharField(max_length=1000),
        ),
    ]
