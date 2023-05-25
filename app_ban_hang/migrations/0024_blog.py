# Generated by Django 3.2.12 on 2023-05-25 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ban_hang', '0023_remove_sanpham_loaisp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('TieuDe', models.CharField(max_length=200)),
                ('NoiDung', models.TextField()),
                ('LuotLike', models.IntegerField(blank=True, default=0, null=True)),
                ('SoCmt', models.IntegerField(blank=True, default=0, null=True)),
                ('NgayDang', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]