from . import statistics
from django import forms


class PredictionForm(forms.Form):
    category_choices,content_choices,genre_choices=statistics.get_choices()
    appName = forms.CharField(label='App Name',widget=forms.TextInput(attrs={'placeholder':'Enter App Name'}))
    size = forms.IntegerField(label='Size',min_value=0,max_value=3000,widget=forms.NumberInput(attrs={'placeholder':'Enter Size (in MB)'}))
    androidVersion = forms.DecimalField(label='Android Version',min_value=1.0, max_value=10.0,widget=forms.NumberInput(attrs={'placeholder':'Enter Android Version'}))
    category = forms.ChoiceField(choices=category_choices,widget=forms.Select(attrs={'class':'regDropDown'}))
    price = forms.DecimalField(label='Price',min_value=0,max_value=10000,widget=forms.NumberInput(attrs={'placeholder':'Enter Price (INR)'}))
    content = forms.ChoiceField(choices=content_choices,widget=forms.Select(attrs={'class':'regDropDown'}))
    genre = forms.ChoiceField(choices=genre_choices,widget=forms.Select(attrs={'class':'regDropDown'}))

