# Generated by Django 4.0.3 on 2023-01-17 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_year', models.CharField(default='', max_length=10)),
                ('intensity', models.IntegerField(default=0)),
                ('sector', models.CharField(default='', max_length=100)),
                ('topic', models.CharField(default='', max_length=100)),
                ('insight', models.CharField(default='', max_length=500)),
                ('url', models.URLField(default='', max_length=400)),
                ('region', models.CharField(default='', max_length=100)),
                ('start_year', models.CharField(default='', max_length=10)),
                ('impact', models.CharField(default='', max_length=100)),
                ('added', models.CharField(default='', max_length=100)),
                ('published', models.CharField(default='', max_length=100)),
                ('country', models.CharField(default='', max_length=100)),
                ('relevance', models.IntegerField(default=0)),
                ('pestle', models.CharField(default='', max_length=50)),
                ('source', models.CharField(default='', max_length=50)),
                ('title', models.CharField(default='', max_length=800)),
                ('likelihood', models.IntegerField(default=0)),
            ],
        ),
    ]
