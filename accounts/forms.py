from django import forms
from .models import *

# Add host profile form
class Add_profile(forms.ModelForm):
    host_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style':'width : 17rem','placeholder':'Name'}), required=True, max_length=50)
    host_email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','style':'width : 17rem','placeholder':'Email Id'}), required=True, max_length=50)
    host_phone = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','style':'width : 17rem','placeholder':'Phone Number'}), required=True, max_length=10)
    host_image = forms.FileField(required = True)
    host_desc = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style':'width : 17rem','placeholder':'Role'}), required=True, max_length=50)
    available = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style':'width : 28rem','placeholder':'Monday - Friday'}), required=True, max_length=50)

    class Meta():
        model = Host
        fields = ['host_name','host_email','host_phone','host_image','host_desc','available']

# Add a meeting form
class Meeting_form(forms.ModelForm):
    visitor_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}), required=True, max_length=50)
    visitor_email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Id'}), required=True, max_length=50)
    visitor_phone = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Phone Number'}), required=True, max_length=10)
    visitor_permissions = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Special Permissions'}), required=True, max_length=100)
    class Meta():
        model = Meeting
        fields = ['visitor_name','visitor_email','visitor_phone','visitor_permissions']
choice = [
    ('yes', 'Yes'),
    ('no', 'No')
    ]

class Visitorform(forms.ModelForm):
    error_css_class = 'error'
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}), required=True, max_length=50)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Id'}), required=True, max_length=50)
    phoneno = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Phone Number'}), required=True)
    company  = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Company name'}), required=True)
    purpose = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Purpose of visit'}), required=True)
    material = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Material Carried'}), required=True)
    time = forms.TimeField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Time Preferred'}), required=True)
    adharno = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Ardharno Number'}), required=True)
    pancardno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Pancard Number'}), required=True)
    licenseno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'License Number'}), required=True)
    image = forms.FileField(required = True)
    adharcard = forms.FileField(required =True)
    pancard = forms.FileField(required = True)
    license = forms.FileField(required = True)
    containment = forms.ChoiceField(choices=choice, required=True)
    symptoms = forms.ChoiceField(choices=choice, required=True)
    history = forms.ChoiceField(choices=choice, required=True)
    family =  forms.ChoiceField(choices=choice, required=True)   
    class Meta():
        model = guest
        fields = ['name','email','phoneno','company','purpose','material','time','adharno','pancardno','licenseno','image','adharcard','pancard','license','containment','symptoms','history','family']


class time(forms.Form):
	timeassigned = forms.CharField(required=True)
	mid = forms.CharField(required=True)




