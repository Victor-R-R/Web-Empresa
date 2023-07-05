from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Nombre', widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu nombre'}
    ), min_length=3)
    email = forms.EmailField(required=True, label='Email',widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu email'}
    ), min_length=3, max_length=100)
    content = forms.CharField(required=True, label='Contenido', widget=forms.Textarea(
        attrs={'class':'form-control', 'rows': 5, 'placeholder':'Escribe tu mensaje'}
    ), min_length=10, max_length=1000)