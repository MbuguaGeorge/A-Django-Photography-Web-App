from django import forms
from .models import Message

class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'sender' : forms.TextInput(attrs={'placeholder' : 'Name'}),
            'email' : forms.TextInput(attrs={'placeholder' : 'Email'}),
            'content' : forms.TextInput(attrs={'placeholder' : 'Type your message here...'})
        }