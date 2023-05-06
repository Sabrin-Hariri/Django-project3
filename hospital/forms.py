from django import forms
from .models  import Patient


class CURDForm(forms.ModelForm):
    fname=forms.CharField(widget=forms.TextInput(attrs={
                "class":"form-control" , "placeholder":" frist name" }))
    lname=forms.CharField(widget=forms.TextInput(attrs={
                "class":"form-control" , "placeholder":" last name" }))
    age=forms.CharField(widget=forms.TextInput(attrs={
                "class":"form-control" , "placeholder":" Age" }) )
    title=forms.CharField(widget=forms.TextInput(attrs={
                "class":"form-control" , "placeholder":" title " }))
    description=forms.CharField(widget=forms.Textarea(attrs={
                "class":"form-control" , "placeholder":" description" }))
    class Meta:
        model=Patient
        fields = '__all__'
