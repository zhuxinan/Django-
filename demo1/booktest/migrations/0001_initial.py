# Generated by Django 2.2 on 2019-04-16 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=20)),
                ('bcontent', models.CharField(max_length=100)),
                ('bpub_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=20)),
                ('hgender', models.BooleanField()),
                ('hcontent', models.CharField(max_length=100)),
                ('hbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktest.Book')),
            ],
        ),
    ]
