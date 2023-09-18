from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django import forms
from accounts.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, label='email')
    date_of_birth = forms.DateField(label='date_of_birth')
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'date_of_birth',
                  'is_active', 'is_staff', 'is_superuser')
