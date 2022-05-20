from django.http import HttpResponse
from django.shortcuts import redirect, render
from numpy import number
from .models import category,product,cart

def home(request):
    allcategory = category.objects.all()
    allproducts = product.objects.all().order_by("-id")
    number =0
    for c in cart.objects.all():
        number =number +int(c.no)
    return render(request,'pages/home.html',{"allproducts":allproducts,"allcategory":allcategory,'number':number})

def Category(request,categoryid):
    allcategory = category.objects.all()
    allproducts = product.objects.all().filter(catagory_id=categoryid).order_by("-id")
    return render(request,'pages/category.html',{"allproducts":allproducts,"allcategory":allcategory})

def Product(request,productid):
    allcategory = category.objects.all()
    allproducts = product.objects.all().filter(id=productid).order_by("-id")    
    return render(request,'pages/product.html',{"allcategory":allcategory,"allproducts":allproducts})

def Cart(request):
    allcategory = category.objects.all()
    allproducts = product.objects.all()
    number =0
    for c in cart.objects.all():
        number =number +int(c.no)
    carts=cart.objects.all()
    return render(request,'pages/cart.html',{'cart':carts,"allproducts":allproducts,'number':number,"allcategory":allcategory})


def addd(request,productid,numb):
    x=int(cart.objects.filter(prod=productid).count())
    if x >= 1:
        s=cart.objects.get(prod=productid)
        cart.objects.filter(prod=productid).update(no=int(s.no)+numb)
    else:
        carts=cart(prod=productid,no=numb)
        carts.save()
    return redirect("/")

def remove(request,proid):
    x=int(cart.objects.filter(prod=proid).count())
    if x!=0:
        q=cart.objects.get(prod=proid)
        if q.no >1:
            cart.objects.filter(prod=proid).update(no=int(q.no)-1)
        else:
            q.delete()
    return redirect("/cart/")