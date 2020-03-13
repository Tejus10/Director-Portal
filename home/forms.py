from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

from .models import *

class DateInput(forms.DateInput):
	input_type = 'date'

class Internal_creation_form(forms.ModelForm):
    class Meta:
    	model = internal_letter
    	fields = [
        	'si_no',
			'in_date',
			'doc_type',
			'reference',
			'From',
			'out_date',
			'to',
			'subject',
			'remarks',
            'referred_to',
        ]
    	widgets = {
            'in_date': DateInput(),
            'out_date':DateInput(),
        }

class External_creation_form(forms.ModelForm):
    class Meta:
        model = external_letter
        fields =[
        	'si_no',
			'receipt_date',
			'From',
			'subject',
			'marked_to',
			'action_needed',
			'file',
			'remarks',
            'referred_to',
        ]
        widgets = {
            'receipt_date': DateInput(),
            
        }        

    