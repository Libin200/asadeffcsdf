# Generated by Django 4.2.4 on 2023-08-20 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='abijith',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('salary', models.IntegerField()),
                ('contact_no', models.BigIntegerField()),
            ],
            options={
                'db_table': 'ABIJITH',
            },
        ),
    ]
