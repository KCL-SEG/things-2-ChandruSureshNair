from django import forms

"""Forms of the project."""

# Create your forms here.
class ThingForm(forms.Form):
  name = forms.CharField(label='Name', max_length=35)
  description = forms.CharField(label='Description', widget=forms.Textarea, max_length=120)
  quantity = forms.IntegerField(label='Quantity', min_value=0, max_value=50)

