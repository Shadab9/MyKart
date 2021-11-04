

# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Product,Contact
from math import ceil

# Create your views here.
def index(request):
    products=Product.objects.all()
    print(products)
    n=len(products)
    params={'product':products}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        print(name,email,phone,desc)
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,'shop/contact.html')
def tracker(request):
    return render(request,'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')
def prodView(request,myid):
    #Fetch the product using id
    product=Product.objects.filter(id=myid)
  
    return render(request,'shop/prodview.html',{'product':product[0]})

def checkout(request):
    return HttpResponse("Checkout")