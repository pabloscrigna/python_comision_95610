from django import forms


class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    camada = forms.IntegerField()
    modalidad = forms.ChoiceField(choices=[
        ('ONL', 'Online'),
        ('PRE', 'Presencial'),
        ('HIB', 'Hibrido')
    ]
    )

