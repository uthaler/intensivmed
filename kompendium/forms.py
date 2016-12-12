from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (FormActions)

from .models import Rechner

class RechnerForm(forms.ModelForm):
    class Meta:
        model = Rechner
        fields = ['natrium', 'kalium']

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-6'
    helper.field_class = 'col-sm-6'
    helper.layout = Layout(
        Field('natrium', css_class='input-sm'),
        Field('kalium', css_class='input-sm'),
        FormActions(Submit('Senden', 'Senden', css_class='btn-primary'))
    )
