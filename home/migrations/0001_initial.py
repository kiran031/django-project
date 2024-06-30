# Generated by Django 5.0.6 on 2024-06-30 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('number', models.CharField(max_length=122)),
                ('disc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
