from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Pic
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'photography/index.html')

def gallery(request):
    p = Pic.objects.all()
    context = {
        'p' : p,
    }
    return render(request, 'photography/gallery.html', context)

def contact(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('home')
    else:
        form = ContactForm()
        return render(request, 'photography/contact.html', {'form' : form})
