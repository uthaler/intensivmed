from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Button
from crispy_forms.bootstrap import (FormActions)
from django.core.exceptions import ValidationError


from .models import Rechner, BGA

class RechnerForm(forms.ModelForm):
    
    class Meta:
        model = Rechner
        fields = ['natrium', 'kalium', 'alter', 'geschlecht', 'kg', 'serumOsmo', 'uosmo', 'unatrium', 'blutzucker', 'bun']

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    #helper.form_show_labels = False # hides the labels
    helper.label_class = 'col-sm-2 col-sm-offset-3'
    helper.field_class = 'col-sm-3' 
    helper.labels_uppercase = False
    helper.layout = Layout(
        Field('natrium', css_class='input-sm', placeholder="S-Na+ mmol/l"),
        Field('kalium', css_class='input-sm', placeholder="S-K+ mmol/l"),
        Field('alter', css_class='input-sm', placeholder="Alter"),
        Field('geschlecht', css_class='input-sm', placeholder="Geschlecht"),
        Field('kg', css_class='input-sm', placeholder="Gewicht"),
        Field('serumOsmo', css_class='input-sm', placeholder="Serum Osmo"),
        Field('uosmo', css_class='input-sm', placeholder="Harn Osmo"),
        Field('unatrium', css_class='input-sm', placeholder="Harn Natrium"),
        Field('blutzucker', css_class='input-sm', placeholder="Blutzucker"),
        Field('bun', css_class='input-sm', placeholder="BUN"),
        FormActions(Submit('Senden', 'Senden', css_class='btn-primary'))
    )

    def clean_natrium(self):
        data = self.cleaned_data['natrium']
        if data > 160:
            raise ValidationError('Falsch!')
        return data

class BGAForm(forms.ModelForm):
    
    class Meta:
        model = BGA
        fields = ['ph', 'bicarbonate', 'pco_two', 'base_excess', 'sodium', 'potassium','chloride', 'albumin', 'phosphate', 'lactate', 'serumOsmo', 'uosmo', 'blutzucker', 'bun', 'sodium_urine', 'potassium_urine', 'chloride_urine', 'urine_ph']

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-2 col-sm-offset-3'
    helper.field_class = 'col-sm-3'
    helper.form_show_labels = True
    helper.layout = Layout(    
        Field('ph', css_class='input-sm'),
        Field('pco_two', css_class='input-sm'),
        Field('bicarbonate', css_class='input-sm'),
        Field('base_excess', css_class='input-sm'),
        Field('sodium', css_class='input-sm'),
        Field('potassium', css_class='input-sm'),
        Field('chloride', css_class='input-sm'),
        Field('albumin', css_class='input-sm'),
        Field('phosphate', css_class='input-sm'),
        Field('lactate', css_class='input-sm'),
        Field('serumOsmo', css_class='input-sm'),
        Field('uosmo', css_class='input-sm'),
        Field('blutzucker', css_class='input-sm'),
        Field('bun', css_class='input-sm'),
        Field('sodium_urine', css_class='input-sm'),
        Field('potassium_urine', css_class='input-sm'),
        Field('chloride_urine', css_class='input-sm'),
        Field('urine_ph', css_class='input-sm'),
        FormActions(Submit('Senden', 'Senden', css_class='btn-primary')),
        )

    def clean_ph(self):
        data = self.cleaned_data['ph']
        if data > 7.8:
            raise ValidationError('impossible!')
        return data
