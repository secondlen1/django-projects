from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Data

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False,help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False,help_text='Optional')
    email = forms.EmailField(max_length=254,help_text='Required. Inform a valid email address.', required=True)

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']

def validate_file_extension(value):
        if not value.name.endswith('.csv'):
            raise forms.ValidationError("Only CSV file is accepted")

class FileForm(forms.Form):
    file = forms.FileField(label='Upload CSV file', validators=[validate_file_extension])


class ChoiceForm(forms.Form):
    choice = forms.ChoiceField(choices=[(1, 'Graphic'),(2, 'Linear Regresion'), (3, 'Polynomn')],label='choose an action')

class GraphicForm(forms.Form):
    xlim_r = forms.IntegerField(label='x right') # set xlim and ylim
    xlim_l = forms.IntegerField(label='x left')
    ylim_r = forms.IntegerField(label='y right')
    ylim_l = forms.IntegerField(label='y left')
    
class MNKForm(GraphicForm):
    k = forms.IntegerField(label='power of polynomn')

    

    