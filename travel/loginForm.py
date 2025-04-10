from django import forms
from django.core.validators import RegexValidator
from .models import RegisterModel

class LoginForm(forms.Form):
    userEmail = forms.CharField(label="Usermail:", max_length=64, required=True,
        widget=forms.EmailInput(attrs={'id':'useremail','class':'form-control','placeholder':'Enter the useremail: '}))

    pswdReg = RegexValidator(
        regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%?&])[A-Za-z\d@$!%*?&]{8,}$',
        message="Password must contain the lowecase, uppercase, numbers, specialsymbols"
    )

    #validators=[pswdReg],
    userPswd = forms.CharField(label="Password: ", max_length=12, required=True,
    widget=forms.PasswordInput(attrs={'id':'userpswd','class':'form-control','placeholder':'Enter the password: '}))

class RegisterForm(forms.ModelForm):
    class Meta:
        model=RegisterModel
        fields='__all__'
        widgets={
            'firstName' : forms.TextInput(attrs={'id':'firstname','class':'form-control','placeholder':'Enter the firstname'}),
            'lastName' : forms.TextInput(attrs={'id':'lastname','class':'form-control','placeholder':'Enter the lastname'}),
            'userEmail' : forms.EmailInput(attrs={'id':'email','class':'form-control','placeholder':'Enter the email'}),
            'userPswd' : forms.PasswordInput(attrs={'id':'password','class':'form-control','placeholder':'Enter the password'}),
            'gender' : forms.RadioSelect(attrs={'id':'gender','class':'form-check-input'}),
            'phoneNumber' : forms.TextInput(attrs={'id':'phno','class':'form-control'}),
        }