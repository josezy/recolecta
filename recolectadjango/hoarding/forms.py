from django import forms

from hoarding.models import Item
from core.constants import WEEKDAYS, WORKING_TIMES

AVAILABILITY = (
    (f"{day[0]}_{wt[0]}", f"{day[1]} {wt[1]}")
    for day in WEEKDAYS for wt in WORKING_TIMES
    if wt[0] in ('morning', 'afternoon', 'night')
)


class ItemForm(forms.ModelForm):
    description = forms.CharField(
        label='Descripción',
        help_text='Detalles del lo que piensas desechar'
    )
    address = forms.CharField(label='Dirección')
    collection_schedule = forms.MultipleChoiceField(
        choices=AVAILABILITY
    )

    class Meta:
        model = Item
        fields = ('description', 'address', 'collection_schedule')
