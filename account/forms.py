from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate
from .models import *
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length = 60)
    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')

class RecruitmentForm(forms.ModelForm):
    class Meta:
        model = RecruitmentApplicant
        fields = ('roll_number', 'batch', 'branch', 'phoneNumber')

class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = Account
        fields = ('email', 'password')
    
    def clean(self):
        # email = self.cleaned_data['email'].lower()
        email = MyAccountManager.normalize_email(self.cleaned_data['email'])
        password = self.cleaned_data['password']
        if not authenticate(email = email, password = password):
            raise forms.ValidationError('Invalid Credentials')

class SandArtRegistrationForm(forms.ModelForm):
    class Meta:
        model = SandArtReg
        fields = "__all__"

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = "__all__"
        widgets = {
            'event' : forms.HiddenInput()
        }
        labels = {
            'event': ''
        }
