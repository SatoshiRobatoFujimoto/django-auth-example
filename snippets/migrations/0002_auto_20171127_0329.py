# Generated by Django 2.0rc1 on 2017-11-26 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, verbose_name='本文')),
                ('commented_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日')),
                ('commented_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='投稿者')),
            ],
        ),
        migrations.AlterField(
            model_name='snippet',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日'),
        ),
        migrations.AddField(
            model_name='comment',
            name='commented_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snippets.Snippet', verbose_name='スニペット'),
        ),
    ]
