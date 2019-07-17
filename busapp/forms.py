from django import forms 
from .models import PassengerRegModel

class PassengerRegForm(forms.ModelForm):
   class Meta:
       model = PassengerRegModel
       fields = ('cname','username','password','membership_type')
       