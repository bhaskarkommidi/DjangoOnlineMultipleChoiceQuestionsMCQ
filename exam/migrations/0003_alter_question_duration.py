# Generated by Django 4.1.2 on 2022-10-18 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_groupquestion_questionset_question_option_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]