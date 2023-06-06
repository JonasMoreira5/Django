from django import forms

class InsereFuncioanarioFor(forms.Form)

    nome = forms.CharField(
        required=True,
        max_length=255
    )
    
    sobrenome = forms.CharField(
        required=True,
        max_length=255
    )
    

    cpf = forms.CharField(
        required=True,
        max_length=14
    )
    
    tempo