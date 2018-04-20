from django import forms


class GesFilterForm(forms.Form):
    max_power = forms.IntegerField(label='Мощность от МВт', required=False)
    min_power = forms.IntegerField(label='Мощность до МВт', required=False)
    max_area = forms.IntegerField(label='Объем от кв.км', required=False)
    min_area = forms.IntegerField(label='Объем до кв.км', required=False)