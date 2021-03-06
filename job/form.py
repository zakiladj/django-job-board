from django import forms
from django.db.models import fields
from .models import Apply,Job


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name','email','website','cv','cover_lettre']
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('slug',)