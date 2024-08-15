from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        # Si queremos EDIAR los mensajes de ayuda editamos este dict,
            # de lo contrario lo limpiamos de ésta forma.
        help_text = {k: "" for k in fields}

class UserEditForm(UserChangeForm):
    password = None  # No mostrar el campo de contraseña
    first_name = forms.CharField(label="Nombre:")
    last_name = forms.CharField(label="Apellido:")
    email = forms.EmailField(label="Email:")
    imagen = forms.ImageField(label="Avatar", required=False)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "imagen"]