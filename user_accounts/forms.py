from django import forms

class Login_form(forms.Form):
    Username= forms.CharField()
    Password=forms.CharField(widget=forms.PasswordInput)

class Signup(forms.Form):
     Username= forms.CharField()
     First_name= forms.CharField()
     Last_name= forms.CharField()
     Password=forms.CharField(widget=forms.PasswordInput)
