# Generated by Django 3.2.10 on 2021-12-25 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0012_participant_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='insurencetype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Insurenctype', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
