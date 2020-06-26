from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm (UserCreationForm):
    email= forms.EmailField()
    first_name= forms.CharField(required=False)
    last_name=forms.CharField(required =False)
    
    class Meta :
        model=User
        fields=['first_name','last_name','username','email','password1','password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is not unique")


class UserUpdateForm(forms.ModelForm):
    email= forms.EmailField()

    class Meta:
        model=User
        fields=['first_name', 'last_name','username','email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model=Profile
        fields=['image','bio']