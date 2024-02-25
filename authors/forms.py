from django import forms
from receps.models import Recipes

class FormsAuthors(forms.ModelForm):

    class Meta:
    
        model = Recipes
        fields = ['title', 'category', 'portions', 'description', 'is_published', 'time']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['title'].widget.attrs.update({'id': 'dash-title','placeholder': 'Exemple title', 'minlength': 6})
        
        self.fields['category'].widget.attrs.update({'id': 'dash-category'})
        
        self.fields['portions'].widget.attrs.update({'id': 'dash-portions', 'placeholder': '1'})
        
        self.fields['description'].widget.attrs.update({'id': 'dash-description', 'placeholder': 'About'})
        
        self.fields['is_published'].widget.attrs.update({'id': 'dash-published'})
        
        self.fields['time'].widget.attrs.update({'id': 'dash-time', 'placeholder': '1h 20m'})