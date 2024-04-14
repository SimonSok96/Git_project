from django import forms
from .models import Tweet, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TweetForm(forms.ModelForm):
    body = forms.CharField(required=True,
                           widget=forms.widgets.Textarea(attrs={"placeholder": "enter your tweet", "class": "form-control"}),
                           label="")
    class Meta:
        model = Tweet
        exclude = ("user",)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.widgets.TextInput(attrs={"placeholder": "enter your email", "class": "form-control"}), label="")
    first_name = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "enter your first name", "class": "form-control"}), label="")
    last_name = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "enter your last name", "class": "form-control"}), label="")
    
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2",)
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
        
        
class ProfileForm(forms.ModelForm):
    profile_image = forms.ImageField(label='profile image')
    
    class Meta:
        model = Profile
        fields = ("profile_image",)
        
        

    