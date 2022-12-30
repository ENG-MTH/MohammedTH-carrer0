from django import forms
from .models import Posts


class NewPost(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Posts
        fields = "__all__"

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )