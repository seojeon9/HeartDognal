from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.core.validators import RegexValidator

class UserForm(UserCreationForm):
    phone_regex = RegexValidator(regex=r'^\d{3}-\d{3,4}-\d{4}$', message="000-0000-0000")
    email = forms.EmailField(label='이메일')
    tel = forms.CharField(validators=[phone_regex], max_length=17)
    name = forms.CharField()
    addr = forms.CharField()
    addr_detail = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'tel', 'name', 'addr', 'addr_detail']
        