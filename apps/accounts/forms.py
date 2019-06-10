from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'is_tyalent', 'is_recruiter', 'is_company', )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)
