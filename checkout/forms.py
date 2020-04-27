from django import forms
from .models import Order


class MakePaymentForm(forms.Form):
    """Fields used for the payment form utlised in stripe."""

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2030)]

    credit_card_number = forms.CharField(
        label='Credit card number', required=True, max_length=16
    )
    cvv = forms.CharField(
        label='Security code (CVV)',
        required=True,
        max_length=3
    )
    expiry_month = forms.ChoiceField(
        label='Month', choices=MONTH_CHOICES, required=True
    )
    expiry_year = forms.ChoiceField(
        label='Year', choices=YEAR_CHOICES, required=True
    )
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    """
    Fields for user to fill out their delivery details in the
    checkout process and move on to payemnt step.
    """

    class Meta:
        model = Order
        fields = (
            'full_name', 'phone_number', 'street_address1', 'street_address2',
            'town_or_city', 'county', 'country', 'postcode'
        )
