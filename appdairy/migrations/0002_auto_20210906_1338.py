# Generated by Django 2.0 on 2021-09-06 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appdairy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField(default='1')),
                ('Total', models.IntegerField(default='500')),
                ('Userid', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='appdairy.User')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pcategory', models.CharField(default='product category', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Productss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pro_name', models.CharField(default='proname', max_length=250)),
                ('Pro_image', models.ImageField(default='xyz.jpg', upload_to='productimage/')),
                ('Pro_weight', models.IntegerField(default='125pabc')),
                ('Pro_weightCat', models.CharField(default='abc', max_length=100)),
                ('Pro_price', models.FloatField()),
                ('Pro_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appdairy.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(default='asd#45', max_length=150)),
                ('Lname', models.CharField(default='lname', max_length=255)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Mobile', models.IntegerField(default='456')),
                ('Address', models.CharField(default='address', max_length=255)),
                ('Password', models.CharField(default='password', max_length=255)),
                ('OTP', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='productss',
            name='sellerid',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='appdairy.Seller'),
        ),
        migrations.AddField(
            model_name='carts',
            name='product',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='appdairy.Productss'),
        ),
    ]
