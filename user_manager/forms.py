from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    id = forms.CharField(label="ID", max_length=12)
    password = forms.CharField(label="PASSWORD", max_length=12)


class RegisterForm(UserCreationForm):

    # username = forms.CharField(label="Your ID")
    # # first password field
    # password1 = forms.CharField(label="Your Password")
    # # confirm password field
    # password2 = forms.CharField(label="Repeat Your Password")
    # email = forms.EmailField(label="Email Address")
    # first_name = forms.CharField(label="First Name")
    # last_name = forms.CharField(label="Last Name")

    username = forms.CharField(label="Your ID")
    # first password field
    password1 = forms.CharField(label="Your Password", widget=forms.PasswordInput())
    # confirm password field
    password2 = forms.CharField(label="Repeat Your Password", widget=forms.PasswordInput())
    email = forms.EmailField(label="Email Address")
    first_name = forms.CharField(label="First Name-")
    last_name = forms.CharField(label="Last Name-")


    # this sets the order of the fields
    class Meta:
        model = User
        # fields = ("first_name", "last_name", "email", "username", "password1", "password2",)
        fields = ("username", "password1", "password2", "first_name", "last_name", "email")

    # this redefines the save function to include the fields you added
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        if commit:
            user.save()
        return user