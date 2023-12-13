from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput)
    password = forms.CharField(max_length=8, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    name_input = forms.CharField(max_length= 20)
    mail_input = forms.EmailField(max_length=255)
    pass_input = forms.CharField(max_length=8, widget=forms.PasswordInput)
    pass2_input = forms.CharField(max_length=8, widget=forms.PasswordInput)