# Generated by Django 3.2 on 2022-12-08 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0007_alter_client_block'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rel_client', to='build.client'),
        ),
    ]
