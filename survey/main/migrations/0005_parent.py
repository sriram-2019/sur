# Generated by Django 4.1.5 on 2023-08-15 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_staff2'),
    ]

    operations = [
        migrations.CreateModel(
            name='parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sd', models.TextField()),
                ('batch', models.TextField()),
                ('occupation', models.TextField()),
                ('vision', models.TextField()),
                ('mission', models.TextField()),
                ('peo', models.TextField()),
                ('pos', models.TextField()),
            ],
        ),
    ]
