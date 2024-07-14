# Generated by Django 5.0.6 on 2024-07-12 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='images/')),
                ('content', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Portfolio',
        ),
        migrations.AddField(
            model_name='team',
            name='content',
            field=models.TextField(default=12),
            preserve_default=False,
        ),
    ]
