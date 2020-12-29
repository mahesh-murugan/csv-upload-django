from django import forms


def validate_file_extension(value):
        if not value.name.endswith('.csv'):
            raise forms.ValidationError("Only CSV file is accepted")


class CSVUploadForm(forms.Form):

    file = forms.FileField(required=True, widget=forms.FileInput(attrs={
        'class': 'form-control input',
        'accept': '.csv'
        }), validators=[validate_file_extension])