# Generated by Django 3.2.8 on 2021-10-24 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0003_auto_20211024_1336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transacao',
            old_name='observaoes',
            new_name='observacões',
        ),
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(),
        ),
    ]
