from django import forms
from django.core import validators

def check_size(value):      #cstm validator
    if len(value) < 6:
        raise forms.ValidationError("the Password is too short")


class SignUp(forms.Form):
    first_name = forms.CharField(initial = 'First Name',)
    last_name = forms.CharField(validators = [validators.MinLengthValidator(6)])        #inline validator
    email = forms.EmailField(help_text = 'write your email',)
    Address = forms.CharField(required = False,)
    Technology = forms.CharField(initial = 'Django', disabled = True,)
    age = forms.IntegerField()
    password = forms.CharField(widget = forms.PasswordInput, validators= [check_size,])
    re_password = forms.CharField(help_text = 're-enater your password', widget = forms.PasswordInput)  #clean_fields_validator

    def clean_re_password(self):
        re_password = self.cleaned_data['re_password']
        if len(re_password) < 4:
            raise forms.ValidationError("password is too short")
        return re_password

    def clean_first_name(self):
        fname = self.cleaned_data['first_name']
        if len(fname) < 10:
            raise forms.ValidationError("minimum lenght 10")
        return fname

        
    def clean(self):                                        #pass and repass check
        cleaned_data = super(SignUp, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("re_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )