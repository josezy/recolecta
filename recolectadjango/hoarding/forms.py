from django import forms

from hoarding.models import Item
from core.constants import PICKUP_TIMES


class ItemForm(forms.ModelForm):
    description = forms.CharField(
        label='Descripción',
        help_text='Detalles del lo que piensas desechar'
    )
    address = forms.CharField(label='Dirección')
    phone = forms.CharField(label='Celular/Fijo')
    pickup_times = forms.MultipleChoiceField(choices=PICKUP_TIMES)

    class Meta:
        model = Item
        fields = ('description', 'address', 'phone', 'pickup_times')
