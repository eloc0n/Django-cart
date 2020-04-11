from django import forms

from .models import UserAddres


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = UserAddres
        fields = ['address',
                    'address2',
                    'city',
                    'country',
                    'zipcode',
                    'phone',
                    # 'shipping',
                    # 'billing',
                    'message']
    def __init__(self, *args, **kwargs):
        super(UserAddressForm, self).__init__(*args, **kwargs)
        self.fields['address'].widget.attrs.update({'class':'form-control'})
        self.fields['address2'].widget.attrs.update({'class':'form-control'})
        self.fields['city'].widget.attrs.update({'class':'form-control'})
        self.fields['country'].widget.attrs.update({'class':'form-control'})
        self.fields['zipcode'].widget.attrs.update({'class':'form-control'})
        self.fields['phone'].widget.attrs.update({'class':'form-control'})
        # self.fields['shipping'].widget.attrs.update({'class':'form-check',
        #                                              'type':'checkbox'})
        # self.fields['billing'].widget.attrs.update({'class':'form-control'})
        self.fields['message'].widget.attrs.update({'class' : 'form-control',
                                                    'id':'exampleFormControlTextarea1',
                                                    'rows':'3'})