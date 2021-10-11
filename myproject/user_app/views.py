from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import Category
from .models import User
from .models import Review

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def register(request):
    newProducts=[]
    viewedProducts=[]
    bestProducts=[]
    buyedProducts=[]
    allProducts=Product.objects.all().order_by('-productAddedDate')
    i=0
    for product in allProducts:
        if product.productQuantity>0:
            newProducts.append(product)
            i+=1
            if i>3:
                break

    allProducts=Product.objects.all().order_by('-productViewed')
    i=0
    for product in allProducts:
        if product.productQuantity>0:
            viewedProducts.append(product)
            i+=1
            if i>3:
                break
    allProducts=Product.objects.all().order_by('-productDiscount')
    i=0
    for product in allProducts:
        if product.productQuantity>0:
            bestProducts.append(product)
            i+=1
            if i>3:
                break
    allProducts=Product.objects.all().order_by('-productBuyed')
    i=0
    for product in allProducts:
        if product.productQuantity>0:
            buyedProducts.append(product)
            i+=1
            if i>3:
                break
    if request.method=='POST':
        newUser=User(
        userName=request.POST['uname'],
        userEmail=request.POST['uemail'],
        userPassword=request.POST['upass'],
        userContact=request.POST['ucontact']
        )
        newUser.save()
        categories=Category.objects.all()
        return render(request,'user_app/index.html',{'categories':categories,'message':'Registered Successfully','bestProducts':bestProducts,'newProducts':newProducts,'viewedProducts':viewedProducts,'buyedProducts':buyedProducts})
    categories=Category.objects.all()
    return render(request,'user_app/index.html',{'categories':categories,'bestProducts':bestProducts,'newProducts':newProducts,'viewedProducts':viewedProducts,'buyedProducts':buyedProducts})
   

def loginUser(request):
    newProducts=[]
    viewedProducts=[]
    bestProducts=[]
    buyedProducts=[]
    allProducts=Product.objects.all().order_by('-productAddedDate')
    i=0
    for product in allProducts:
        if product.productQuantity>0:
            newProducts.append(product)
            i+=1
            if i>3:
                break

    allProducts=Product.objects.all().order_by('-productViewed')
    i=0
    for product in allProducts:
        if product.productQuantity>0:
            viewedProducts.append(product)
            i+=1
            if i>3:
                break
    allProducts=Product.objects.all().order_by('-productDiscount')
    i=0
    for product in allProducts:
        if product.productQuantity>0:
            bestProducts.append(product)
            i+=1
            if i>3:
                break
    allProducts=Product.objects.all().order_by('-productBuyed')
    i=0
    for product in allProducts:
        if product.productQuantity>0:
            buyedProducts.append(product)
            i+=1
            if i>3:
                break
    categories=Category.objects.all()
    print("Helloooo")
    if request.method=='POST':
        print("Helloooo")
        userEmail=request.POST['uemail']
        userPassword=request.POST['upass']
        post = User.objects.filter(userEmail=userEmail,userPassword=userPassword)
        if post:
            request.session['userEmail'] = userEmail
            for us in post:         
                request.session['userName'] = us.userName
        else:
            return render(request,'user_app/index.html',{'categories':categories,'message':'Incorrect Password','bestProducts':bestProducts,'newProducts':newProducts,'viewedProducts':viewedProducts,'buyedProducts':buyedProducts})
    if request.session.has_key('userName'):
        userName=request.session['userName']
        return render(request,'user_app/index.html',{'categories':categories,'userName':userName,'bestProducts':bestProducts,'newProducts':newProducts,'viewedProducts':viewedProducts,'buyedProducts':buyedProducts})
    return render(request,'user_app/index.html',{'categories':categories,'bestProducts':bestProducts,'newProducts':newProducts,'viewedProducts':viewedProducts,'buyedProducts':buyedProducts})

def logout(request):
    del request.session['userName']
    del request.session['userEmail']
    return redirect("index")