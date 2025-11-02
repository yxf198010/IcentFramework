from django import forms
from .models import UserGroup

class UserGroupForm(forms.ModelForm):
    class Meta:
        model = UserGroup
        fields = ['usergroup_name','usergroup_desc']