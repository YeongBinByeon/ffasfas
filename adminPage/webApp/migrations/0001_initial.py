# Generated by Django 3.0.2 on 2020-03-11 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utterance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('language', models.CharField(max_length=20)),
                ('mainAction', models.CharField(max_length=50)),
                ('utterance', models.CharField(max_length=100)),
            ],
        ),
    ]
