# Generated by Django 4.0.2 on 2022-02-07 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoomManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(blank=True, upload_to='media')),
                ('phone_no', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
            ],
        ),
    ]