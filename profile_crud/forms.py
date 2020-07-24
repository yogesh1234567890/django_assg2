from django.forms import ModelForm
from .models import profile


class ProfileForm(ModelForm):
    class Meta:
        model = profile
        fields = '__all__'
        # exclude = ['user']
