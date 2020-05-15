# Generated by Django 2.2.1 on 2020-05-15 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_sector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floor',
            name='facility_id_FK',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Floor_facility', to='webapp.Facility'),
        ),
        migrations.AlterField(
            model_name='floor',
            name='floor_no',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Sector',
        ),
    ]