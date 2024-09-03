from django import forms
from .models import *    # * -> is used to models.py la irukka ella class ium use pannikalam
from django.contrib.auth.forms import UserCreationForm    #authendication kkaga

#Notes Page
class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']    #user not require


#Homework Page
    #for DateInput widgets kaga
class DateInput(forms.DateInput):
    input_type = 'date'


class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {'due':DateInput()}
        fields =  ['subject', 'title', 'description', 'due', 'is_finished']

   
#Youtube Page    /    Books Page    /    Dictionary Page    /    Wikipedia Page
class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100, label="Enter Your Search ")


#Todo Page
class TodoForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields =  ['title', 'is_finished']


#Conversion Page
class ConversionForm(forms.Form):
    CHOICES = [('length','Length'),('mass','Mass')] #Radio button
    measurement = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    #for conversion form length
class ConversionLengthForm(forms.Form):
     CHOICES = [('yard','Yard'),('foot','Foot')]
     input = forms.CharField(required=False, label=False, widget=forms.TextInput(
         attrs={'type':'number', 'placeholder':'Enter the Number'}
     ))
     measure1 = forms.CharField(
         label='', widget=forms.Select(choices=CHOICES)
     )
     measure2 = forms.CharField(
         label='', widget=forms.Select(choices=CHOICES)
     )


    #for conversion form mass
class ConversionMassForm(forms.Form):
     CHOICES = [('pound','Pound'),('kilogram','Kilogram')]
     input = forms.CharField(required=False, label=False, widget=forms.TextInput(
         attrs={'type':'number', 'placeholder':'Enter the Number'}
     ))
     measure1 = forms.CharField(
         label='', widget=forms.Select(choices=CHOICES)
     )
     measure2 = forms.CharField(
         label='', widget=forms.Select(choices=CHOICES)
     )


#UserCreationForm for login, logout, register and authendication
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']