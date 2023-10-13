from django.forms import ModelForm
from my_website.models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']