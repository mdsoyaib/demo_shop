# Generated by Django 3.2.7 on 2021-09-01 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='uploads/product')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
            ],
        ),
    ]
