# Generated by Django 3.2.9 on 2021-11-18 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0005_alter_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], default='d', max_length=50, verbose_name='Status'),
        ),
    ]
