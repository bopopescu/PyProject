# Generated by Django 2.1.5 on 2019-02-28 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VMwareAPI', '0003_vmvirtual_vmstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datasotrename', models.CharField(max_length=500)),
                ('hostname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VMwareAPI.VMHost')),
            ],
            options={
                'db_table': 'DataStore',
            },
        ),
    ]
