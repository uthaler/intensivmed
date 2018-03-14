# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-03-09 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kompendium', '0022_delete_calcs'),
    ]

    operations = [
        migrations.CreateModel(
            name='BGA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ph', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('bicarbonate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='HCO3')),
                ('pco_two', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='pCO2')),
                ('base_excess', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='BE')),
                ('lactate', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Lactate')),
                ('sodium', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Na')),
                ('potassium', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='K')),
                ('chloride', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Cl')),
                ('albumin', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Albumin')),
                ('phosphate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='PO4')),
                ('po_two', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='pO2')),
                ('ag_albumin_correction', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Anion gap (corrected for albumin)')),
                ('base_excess_elyte', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='BE electrolytes')),
                ('base_excess_albumin', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='BE albumin')),
                ('base_excess_lactate', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='BE lactate')),
                ('base_excess_uma', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='BE unmeasured anions')),
                ('chloride_urine', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='U-Cl')),
                ('sodium_urine', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='U-Na')),
                ('potassium_urine', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='U-K')),
                ('urine_SID', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='U-SID')),
                ('urine_ph', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='U-pH')),
                ('met_acid_pco_two_expected', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Metabolic acidosis pCO2')),
                ('met_alk_pco_two_expected', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Metabolic alkalosis pCO2')),
                ('acute_resp_acid_bicarbonate_expected', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Acute respiratory acidosis HCO3')),
                ('chronic_resp_acid_bicarbonate_expected', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Chronic respiratory acidosis HCO3')),
                ('chronic_resp_acid_be_expected', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Chronic respiratory acidosis BE')),
                ('acute_resp_alk_bicarbonate_expected', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Acute respiratory alkalosis HCO3')),
                ('chronic_resp_alk_bicarbonate_expected', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Chronic respiratory alkalosis HCO3')),
                ('chronic_resp_alk_be_expected', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Chronic respiratory alkalosis BE')),
            ],
        ),
        migrations.AlterField(
            model_name='rechner',
            name='geschlecht',
            field=models.BooleanField(choices=[(True, 'maennlich'), (False, 'weiblich')], default=True, verbose_name='Gender'),
        ),
    ]
