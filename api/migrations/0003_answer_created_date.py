# Generated by Django 4.1.3 on 2022-11-16 20:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user_bio_user_pet_amount_user_pet_types_question_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 11, 16, 20, 35, 51, 103045, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
