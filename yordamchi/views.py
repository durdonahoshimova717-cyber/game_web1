from django.shortcuts import render
from .models import Mahsulot, Haqida, Reklama

# Create your views here.
def mahsulot(request):
    return render(request, 'product.html')


def asosiy(request):
    context = {
        'asosiy': Reklama.objects.all(),
        'mahsulot': Mahsulot.objects.all(),
        'haqida': Haqida.objects.all(),
    }
    return render(request, 'index.html', context)

def haqida(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def product(request):
    return render(request, 'product.html')

def reklama(request):
    return render(request, 'reklama.html')

def video(request):
    return render(request, 'video.html')

def remot(request):
    return render(request, 'remot.html')



