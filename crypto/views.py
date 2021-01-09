from django.shortcuts import render
from . models import VC
import cryptocompare
# Create your views here.

def home(request):
    mimi = cryptocompare.get_price('XRP',curr='USDT')
    momo = (mimi['XRP'])
    mumu = (momo['USDT'])

    orderlist = VC.objects.all()

    

    return render(request, 'home.html', {'objs':orderlist, 'mumu':mumu})
