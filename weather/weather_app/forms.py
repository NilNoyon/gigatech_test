from django import forms
from .models import *


class WeatherRecordForm(forms.ModelForm):
    class Meta:
        model = WeatherRecord
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(WeatherRecordForm, self).__init__(*args, **kwargs)
 