# Generated by Django 5.2.4 on 2025-07-09 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='age',
        ),
        migrations.RemoveField(
            model_name='game',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='game',
            name='player_count',
        ),
        migrations.RemoveField(
            model_name='game',
            name='playtime',
        ),
        migrations.RemoveField(
            model_name='game',
            name='rules_pdf',
        ),
        migrations.RemoveField(
            model_name='game',
            name='short_description',
        ),
        migrations.AddField(
            model_name='game',
            name='description',
            field=models.TextField(default='vakzhak'),
        ),
        migrations.AddField(
            model_name='game',
            name='marketplace_links',
            field=models.JSONField(default={'ozon': 'url'}),
        ),
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='game',
            name='slug',
            field=models.SlugField(default='vakzhak-game'),
        ),
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(default='Vakzhak', max_length=100),
        ),
    ]
