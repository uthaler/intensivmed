from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Button
from crispy_forms.bootstrap import (FormActions)
from django.core.exceptions import ValidationError


from .models import Rechner

class RechnerForm(forms.ModelForm):
    
    class Meta:
        model = Rechner
        fields = ['natrium', 'kalium', 'alter', 'geschlecht', 'kg', 'serumOsmo', 'uosmo', 'unatrium', 'blutzucker', 'bun']

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-6'
    helper.field_class = 'col-sm-6'
    helper.labels_uppercase = True
    helper.layout = Layout(
        Field('natrium', css_class='input-sm'),
        Field('kalium', css_class='input-sm'),
        Field('alter', css_class='input-sm'),
        Field('geschlecht', css_class='input-sm'),
        Field('kg', css_class='input-sm'),
        Field('serumOsmo', css_class='input-sm'),
        Field('uosmo', css_class='input-sm'),
        Field('unatrium', css_class='input-sm'),
        Field('blutzucker', css_class='input-sm'),
        Field('bun', css_class='input-sm'),
        FormActions(Submit('Senden', 'Senden', css_class='btn-primary'))
    )

    def clean_natrium(self):
        data = self.cleaned_data['natrium']
        if data > 160:
            raise ValidationError('Falsch!')
        return data
