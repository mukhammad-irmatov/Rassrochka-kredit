from django import forms
from .models import Users_Message

class ContactForm(forms.ModelForm):
    class Meta:
        model = Users_Message
        fields = "__all__"