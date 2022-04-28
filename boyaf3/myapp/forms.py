from django import forms
from .models import FileUpload


class UploadFileForm(forms.ModelForm):
    #form = forms.FileField()

    class Meta:
        model = FileUpload
        fields = ['file']
