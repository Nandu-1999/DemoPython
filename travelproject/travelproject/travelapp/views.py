#from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Member
# Create your views here.
def demo(request):
    obj =  Place.objects.all()
    obj2 = Member.objects.all()
    return render(request,"index.html",{'result':obj,'result2' : obj2})
'''def addition(request):
    x = int(request.GET['n1'])
    y = int(request.GET['n2'])
    add_res = x + y
    sub_res = x - y
    mult_res = x * y
    div_res = x/y
    return render(request, "about.html",{'Add_res':add_res,
                                         'Sub_res':sub_res,
                                         'Mul_res':mult_res,
                                        'Div_res':div_res})'''
