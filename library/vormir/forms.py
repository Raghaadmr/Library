from django import forms
from .models import Library, Book , Member
from django.contrib.auth.models import User


class MembershipForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' ,'password']

        widgets={
        'password': forms.PasswordInput(),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class SigninForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

class BorrowedForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
