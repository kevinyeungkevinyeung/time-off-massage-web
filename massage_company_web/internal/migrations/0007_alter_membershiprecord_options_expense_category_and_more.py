# Generated by Django 4.1 on 2022-08-24 14:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0006_alter_transaction_options_alter_transaction_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='membershiprecord',
            options={'ordering': ['-transaction_date']},
        ),
        migrations.AddField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('salary', 'Salary'), ('rent', 'Rent'), ('utilties', 'utilities'), ('marketing', 'Marketing'), ('promotion', 'Promotion'), ('others', 'Others')], default=django.utils.timezone.now, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expense',
            name='report_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
