from django import forms

"""Forms of the project."""

# Create your forms here.
class ThingForm(forms.Form):
  name = forms.CharField(label='Name', max_length=35)
  description = forms.CharField(label='Description', widget=forms.Textarea)
  quantity = forms.IntegerField(label='Quantity')

