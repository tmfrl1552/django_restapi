# Generated by Django 3.0.3 on 2020-06-02 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uimage', models.ImageField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='MyImage',
        ),
    ]
