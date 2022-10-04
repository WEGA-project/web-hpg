# Generated by Django 4.1 on 2022-09-14 10:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0010_plantprofileshares'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantprofilehistory',
            name='history_image2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='plantprofilehistory',
            name='history_image3',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='plantprofilehistory',
            name='history_image4',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='plantprofileshares',
            name='enabled',
            field=models.BooleanField(default=True, verbose_name='Включен/активен'),
        ),
        migrations.AlterField(
            model_name='plantprofileshares',
            name='link_name',
            field=models.CharField(default=uuid.uuid4, max_length=100, unique=True, verbose_name='Имя ссылки'),
        ),
        migrations.AlterField(
            model_name='plantprofileshares',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.plantprofile', verbose_name='Профиль'),
        ),
    ]
