from django import forms
from app.models import Teclado, Mouse, Auricular, Mousepad

class TecladoForm(forms.ModelForm):
    class Meta:
        model = Teclado
        fields = ['nombre', 'tipo', 'descripcion', 'fecha', 'precio']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(choices=Teclado.TIPOS_DE_TECLADO, attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'cols': 80, 'rows': 3}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class MouseForm(forms.ModelForm):
    class Meta:
        model = Mouse
        fields = ['nombre', 'tipo', 'descripcion', 'fecha', 'precio']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(choices=Mouse.TIPOS_DE_MOUSE, attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'cols': 80, 'rows': 3}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class AuricularForm(forms.ModelForm):
    class Meta:
        model = Auricular
        fields = ['nombre', 'tipo', 'descripcion', 'fecha', 'precio']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(choices=Auricular.TIPOS_DE_AURICULAR, attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'cols': 80, 'rows': 3}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class MousepadForm(forms.ModelForm):
    class Meta:
        model = Mousepad
        fields = ['nombre', 'tipo', 'descripcion', 'fecha', 'precio']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(choices=Mousepad.TIPOS_DE_MOUSEPAD, attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'cols': 80, 'rows': 3}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }
