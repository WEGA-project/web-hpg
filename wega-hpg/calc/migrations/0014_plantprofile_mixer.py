# Generated by Django 4.1 on 2022-10-03 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mixer', '0005_mixer_z_p1_mixer_z_p2_mixer_z_p3_mixer_z_p4_and_more'),
        ('calc', '0013_plantprofilehistory_history_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantprofile',
            name='mixer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mixer.mixer'),
        ),
    ]
