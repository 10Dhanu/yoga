from django import forms

from .models import Booking

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your name', 
            'class': 'common-input mb-20 form-control',
            'onfocus': "this.placeholder = ''", 
            'onblur': "this.placeholder = 'Enter your name'"
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter email address', 
            'class': 'common-input mb-20 form-control',
            'pattern': "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{1,63}$",
            'onfocus': "this.placeholder = ''", 
            'onblur': "this.placeholder = 'Enter email address'"
        })
    )
    subject = forms.CharField(
        max_length=200, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter subject', 
            'class': 'common-input mb-20 form-control',
            'onfocus': "this.placeholder = ''", 
            'onblur': "this.placeholder = 'Enter subject'"
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter Message', 
            'class': 'common-textarea form-control',
            'onfocus': "this.placeholder = ''", 
            'onblur': "this.placeholder = 'Enter Message'"
        })
    )

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'location', 'instructor', 'date', 'time', 'user_name', 'user_email', 'phone']
        widgets = {
            'service': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'instructor': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'time': forms.TimeInput(attrs={'class': 'form-control'}),
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'user_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }