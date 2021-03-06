# Generated by Django 3.1.3 on 2020-11-09 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('name', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('value', models.IntegerField()),
                ('min_coast', models.IntegerField()),
                ('start_at', models.DateField(auto_now_add=True)),
                ('finish_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('type', models.CharField(choices=[('fruits', 'fruits'), ('vegetables', 'vegetables')], max_length=20, null=True)),
                ('price', models.FloatField()),
                ('discount_price', models.IntegerField()),
                ('discount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.user')),
            ],
            options={
                'unique_together': {('user', 'product')},
            },
        ),
    ]
