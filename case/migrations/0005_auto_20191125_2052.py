# Generated by Django 2.2.6 on 2019-11-25 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0004_auto_20191123_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='casestatus',
            name='InspectorUpdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='casestatus',
            name='dataEntryUpdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
