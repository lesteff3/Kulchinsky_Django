# Generated by Django 4.0.4 on 2022-06-05 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cw21', '0005_hobby_person_hobbies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_album', models.CharField(default=None, max_length=255)),
                ('year', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_track', models.CharField(default=None, max_length=255)),
                ('value_track', models.FloatField(default=None, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MusicBand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('style_music', models.CharField(max_length=35)),
                ('year', models.PositiveSmallIntegerField()),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='musicband', to='cw21.album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='track',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='album', to='cw21.track'),
        ),
    ]