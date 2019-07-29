from django import forms
from .models import Profile,Image,Comments

class NewImage(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['post_date','user','likes']

class UpdateProfile(forms.ModelForm):
     class Meta:
         model = Profile

class NewComment(forms.ModelForm):
    class Meta:
        model=Comments
        exclude=['user','images']