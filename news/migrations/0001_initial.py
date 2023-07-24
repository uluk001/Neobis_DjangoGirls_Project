# Generated by Django 4.2.3 on 2023-07-24 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Name:')),
                ('content', models.TextField(verbose_name='Content:')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created at:')),
            ],
        ),
    ]