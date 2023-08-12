from django import forms
from .models import ContactProfile
 

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactProfile
        fields = ('name', 'email', 'message','subject', 'phone')

    name = forms.CharField(max_length=100, required=True,
        widget=forms.TextInput(attrs={
            
                'placeholder':"Name",
                'name':"name",
                'id':"name",
                'autocomplete':"off",
                'required':'required'
            }))
    email = forms.EmailField(max_length=254, required=True, 
        widget=forms.TextInput(attrs={
      
                    'id':"emailHelp",
                    'name':"emailHelp",
                    'placeholder':"Email",
                    'autocomplete':"off",
                    'required':'required',
        }))
   
    phone =  forms.CharField(max_length=100, required=True,
        widget=forms.TextInput(attrs={
            
               
                 "type":"tel",
                    "placeholder":"Phone",
                    "name":"phone",
                    "id":"phone",
                    'required':'required'
            }))
    subject =  forms.CharField(max_length=100, required=True,
        widget=forms.TextInput(attrs={
            
               
                "name":"subject",
                "placeholder":"Subject",
                "id":"subject"
            }))
    
   
    message = forms.CharField(max_length=1000, required=True, 
        widget=forms.Textarea(attrs={
            
        'placeholder':"Message",
        'rows':"3",
        'name':"comments",
        'id':"comments"
                
            }))


	