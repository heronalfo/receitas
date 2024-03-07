from django import forms
from receps.models import Recipes
from .models import Authors

class FormsAuthors(forms.ModelForm):

    class Meta:
    
        model = Recipes
        fields = ['title', 'category', 'portions', 'description', 'time', 'cover']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['cover'].widget.attrs.update({'id': 'cover'})
        
        self.fields['title'].widget.attrs.update({'id': 'dash-title','placeholder': 'Exemple title', 'minlength': 6})
        
        self.fields['category'].widget.attrs.update({'id': 'dash-category'})
        
        self.fields['portions'].widget.attrs.update({'id': 'dash-portions', 'placeholder': '1'})
        
        self.fields['description'].widget.attrs.update({'id': 'dash-description', 'placeholder': 'About'})
                      
        self.fields['time'].widget.attrs.update({'id': 'dash-time', 'placeholder': '1h 20m'})
        
        def save(self, commit=True):
        
            instance = super().save(commit=False)
            if self.cleaned_data['cover']:
            
                instance.cover = self.cleaned_data['cover']
                
            if commit:
                instance.save()
                
            return instance

class FormsAuthorsEdit(forms.ModelForm):
    
    class Meta:
    
        model = Authors
        fields = ['name', 'bio', 'link']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs.update({'id': 'author-name', 'placeholder': 'Your user name'})
        
        self.fields['bio'].widget.attrs.update({'id': 'author-bio', 'placeholder': 'Your bio'}})
        
        self.fields['link'].widget.attrs.update({'id': 'author-link', 'placeholder': 'Links for yours redes sociales'}})