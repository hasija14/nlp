from django import forms
from first_app.models import UserInfo
class FormName(forms.Form):
    Tweet_Search=forms.CharField(label="Tweet Search",widget=forms.TextInput(attrs={'class':'form-control','size':100}))

class MyForm(forms.Form):
    My_Tweet=forms.CharField(label="Enter Your Tweet Here",widget=forms.TextInput(attrs={'size':100}))

class MMForm(forms.ModelForm):
    class Meta:
        model=UserInfo
        fields="__all__"
        widgets={
        'Name':forms.TextInput(
        attrs={'class':'form-control','size':50,'placeholder':'Enter Your Name'})
        ,'DOB':forms.TextInput(
        attrs={'class':'form-control','size':50,'placeholder':'YYYY-MM-DD'})
        ,
        'Email':forms.TextInput(
        attrs={'class':'form-control','size':50,'placeholder':'Enter you Email'}),

        'Contact':forms.TextInput(
        attrs={'class':'form-control','size':50,'placeholder':'Enter you Mobile No.'})}
