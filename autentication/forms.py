from django import forms

class UsersForm(forms.Form):

    email = forms.EmailField(min_length=8, max_length=102, required=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['email'].widget.attrs.update({'placeholder': 'exemplo@gmail.com', 'id': 'id_email'})