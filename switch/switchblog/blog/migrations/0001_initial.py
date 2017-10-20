# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 12:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('useraccount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.CharField(max_length=2000)),
                ('date_posted', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(choices=[('Ent', 'Entertainment'), ('Tech', 'Technology'), ('biz', 'Business')], max_length=125)),
                ('is_fetched', models.BooleanField(default=False)),
                ('source', models.CharField(max_length=75, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
                ('date_posted', models.DateTimeField(auto_now=True)),
                ('comment_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useraccount.UserAccount')),
                ('post_attached', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_liked', models.DateTimeField(auto_now=True)),
                ('liked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useraccount.UserAccount')),
                ('post_attached', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='post/images')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='images',
            field=models.ManyToManyField(to='blog.PostImage'),
        ),
        migrations.AddField(
            model_name='blog',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useraccount.UserAccount'),
        ),
    ]
