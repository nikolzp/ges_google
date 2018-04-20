from django.shortcuts import render
from .models import Ges
from .forms import GesFilterForm


def ges_list(request):
    ges = Ges.objects.all()
    form = GesFilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data['max_power']:
            ges = ges.filter(power__gte=form.cleaned_data['max_power'])
        if form.cleaned_data['min_power']:
            ges = ges.filter(power__lte=form.cleaned_data['min_power'])
        if form.cleaned_data['max_area']:
            ges = ges.filter(area_reservoir__gte=form.cleaned_data['max_area'])
        if form.cleaned_data['min_area']:
            ges = ges.filter(area_reservoir__lte=form.cleaned_data['min_area'])
    return render(request,'index.html', {'data': ges, 'form': form})



