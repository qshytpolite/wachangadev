from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your name',
            'class': 'sw-input',
            'autocomplete': 'name',
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'your@email.com',
            'class': 'sw-input',
            'autocomplete': 'email',
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'What are you working on?',
            'class': 'sw-input sw-textarea',
            'rows': 6,
        })
    )
