# Generated by Django 2.2.5 on 2019-11-02 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20191102_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='None', upload_to='news_images/', verbose_name='изображение'),
        ),
        migrations.DeleteModel(
            name='ArticleImage',
        ),
    ]
