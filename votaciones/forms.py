from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroForm(UserCreationForm):
    """El documento de identidad se guarda como nombre de usuario."""
    first_name = forms.CharField(max_length=60, label="Nombre completo")
    email = forms.EmailField(label="Correo electrónico")

    class Meta:
        model = User
        fields = ("username", "first_name", "email", "password1", "password2")
        labels = {"username": "Documento de identidad"}
        help_texts = {"username": ""}

    def clean_username(self):
        doc = self.cleaned_data["username"].strip()
        if not doc.isdigit() or len(doc) < 6:
            raise forms.ValidationError("Ingresa un documento válido (solo números, mínimo 6).")
        return doc

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"inputmode": "numeric", "autocomplete": "off"})
        self.fields["password1"].help_text = ""
        self.fields["password2"].help_text = ""
