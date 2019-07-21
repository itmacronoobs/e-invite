from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    input_excel = forms.FileField()
    update = forms.BooleanField(required=False)