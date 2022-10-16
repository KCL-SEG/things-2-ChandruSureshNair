from django.shortcuts import render
from .forms import ThingForm
from .models import Thing

def home(request):
    if request.method == 'POST':
        form = ThingForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            quantity = form.cleaned_data['quantity']
            thing = Thing(name=name, description=description, quantity=quantity)
            thing.save()
            form = ThingForm()
    else:
        form = ThingForm()
    return render(request, 'home.html', {'form': ThingForm()})
