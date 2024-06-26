# Generated by Django 5.0.3 on 2024-06-02 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.PositiveSmallIntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('archived', models.BooleanField(default=False)),
            ],
        ),
    ]
