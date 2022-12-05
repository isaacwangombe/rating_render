from cProfile import label
from django import forms
from .models import Profile, Projects, Review


class ProjectForm(forms.ModelForm):
  class Meta:
    model = Projects
    exclude = ['user']


class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']

    
class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    exclude = ['user', 'project', 'profile']