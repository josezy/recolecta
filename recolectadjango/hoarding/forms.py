from django import forms

from hoarding.models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('description', 'address')
