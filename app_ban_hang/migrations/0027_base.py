# Generated by Django 3.2.12 on 2023-05-28 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ban_hang', '0026_tuvannoithat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SDT', models.IntegerField(null=True)),
                ('Logo_web', models.ImageField(blank=True, null=True, upload_to='')),
                ('DiaChiCuaHang', models.CharField(max_length=100, null=True)),
                ('HoTroKhachHang', models.CharField(max_length=100, null=True)),
                ('LienHeChungToi', models.CharField(max_length=100, null=True)),
                ('DiaChi_Khac', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
