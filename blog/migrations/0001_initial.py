# Generated by Django 3.0.4 on 2020-03-21 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('head0', models.CharField(default='', max_length=500)),
                ('chead0', models.CharField(default='', max_length=5000)),
                ('head1', models.CharField(default='', max_length=500)),
                ('chead1', models.CharField(default='', max_length=5000)),
                ('head2', models.CharField(default='', max_length=500)),
                ('chead2', models.CharField(default='', max_length=5000)),
                ('pub_date', models.DateField()),
                ('thumbnail', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
