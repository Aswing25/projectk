# Generated by Django 4.2.4 on 2023-09-22 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(blank=True, max_length=50, null=True)),
                ('eage', models.IntegerField(blank=True, null=True)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('company', models.CharField(blank=True, max_length=50, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
