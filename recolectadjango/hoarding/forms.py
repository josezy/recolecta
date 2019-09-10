from django import forms

from hoarding.models import Item


AVAILABILITY = (
    ('monday_morning', 'Lunes 6am - 12m'),
    ('monday_afternoon', 'Lunes 12m - 6pm'),

    ('tuesday_morning', 'Martes 6am - 12m'),
    ('tuesday_afternoon', 'Martes 6am - 12m'),

    # ('monday_morning', 'Lunes 6am - 12m'),
    # ('monday_morning', 'Lunes 6am - 12m'),

    # ('monday_morning', 'Lunes 6am - 12m'),
    # ('monday_morning', 'Lunes 6am - 12m'),

    # ('monday_morning', 'Lunes 6am - 12m'),
    # ('monday_morning', 'Lunes 6am - 12m'),

    # ('monday_morning', 'Lunes 6am - 12m'),
    # ('monday_morning', 'Lunes 6am - 12m'),

    # ('monday_morning', 'Lunes 6am - 12m'),
    # ('monday_morning', 'Lunes 6am - 12m'),
)


class ItemForm(forms.Form):
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
