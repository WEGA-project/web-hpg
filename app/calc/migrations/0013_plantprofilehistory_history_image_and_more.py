# Generated by Django 4.1 on 2022-09-19 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('calc', '0012_remove_plantprofilehistory_history_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantprofilehistory',
            name='history_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='plantprofilehistory',
            name='history_image2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='plantprofilehistory',
            name='history_image3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='plantprofilehistory',
            name='history_image4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image'),
        ),
    ]
