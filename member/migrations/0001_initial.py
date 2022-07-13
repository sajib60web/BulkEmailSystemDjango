# Generated by Django 4.0.6 on 2022-07-12 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('website_url', models.CharField(max_length=50)),
                ('join_date', models.DateField()),
            ],
            options={
                'db_table': 'members',
            },
        ),
    ]