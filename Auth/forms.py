from django import forms
from Auth.models import UserInfo


class UserInfoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = UserInfo
        fields = ('name', 'email', 'password')
