from django.forms import forms
from django.forms.fields import ChoiceField
from getpaid.models import Payment

class DummyQuestionForm(forms.Form):
    """
    This dummy form asks for payment authorization.
    """
    authorize_payment = ChoiceField(choices=((0, 'no'),(1, 'yes')))