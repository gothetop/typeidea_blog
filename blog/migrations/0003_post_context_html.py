# Generated by Django 5.0.2 on 2024-02-22 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_pv_post_uv'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='context_html',
            field=models.TextField(blank=True, editable=False, verbose_name='正文html代码'),
        ),
    ]
