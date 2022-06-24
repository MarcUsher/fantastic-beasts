from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Walk, User

class WalkForm(ModelForm):
  class Meta:
    model = Walk
    fields = ['date', 'distance']


class NewUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
  
  def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
          user.save()
        return user
