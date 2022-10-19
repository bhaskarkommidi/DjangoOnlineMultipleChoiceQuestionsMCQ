# Generated by Django 4.1.2 on 2022-10-18 17:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='exam.question')),
            ],
            bases=('exam.question',),
        ),
        migrations.CreateModel(
            name='QuestionSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_name', models.CharField(max_length=100)),
                ('set_slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('enable_negative_marking', models.BooleanField(default=False)),
                ('negative_marking_percentage', models.IntegerField()),
                ('idealtimetocomplete', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='option_image',
            field=models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png'])]),
        ),
        migrations.AddField(
            model_name='question',
            name='question_image',
            field=models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png'])]),
        ),
        migrations.AddField(
            model_name='question',
            name='question_marks',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='question',
            name='question_order',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('MCQWithRadio', 'MCQWithRadio'), ('MCQWithCheckBox', 'MCQWithCheckBox'), ('Matrix', 'Matrix')], default='MCQWithRadio', max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='groupInlineQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_order', models.IntegerField()),
                ('question_marks', models.IntegerField()),
                ('id_group_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.groupquestion')),
                ('id_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_question', to='exam.question')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='id_questionset',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exam.questionset'),
        ),
    ]
