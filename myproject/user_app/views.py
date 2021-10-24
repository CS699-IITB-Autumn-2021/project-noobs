
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
from .models import Category
from .models import User
from .models import Review
# Create your views here.
def index(request):
    """
     This method controls the index page.

     :param name: request
     :type request: Implicit.
     :returns:  render -- index.html page according to if else conditions.

    .. note::
       This method gets details of products from the **database**.
    """
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
    if request.session.has_key('userName'):
        userName=request.session['userName']
        return render(request,'index.html',{'categories':categories,'userName':userName,'bestProducts':bestProducts,'newProducts':newProducts,'viewedProducts':viewedProducts,'buyedProducts':buyedProducts})
    return render(request,'index.html',{'categories':categories,'newProducts':newProducts,'bestProducts':bestProducts,'viewedProducts':viewedProducts,'buyedProducts':buyedProducts})



def register(request):
    """
     This method takes to registeration page.

     :param name: request
     :type request: Implicit.
     :returns:  render -- index.html with successful registeration message.

    .. note::
       We are using **post** method and some conditions like not null .
    """
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
        return render(request,'index.html',{'categories':categories,'message':'Registered Successfully','bestProducts':bestProducts,'newProducts':newProducts,'viewedProducts':viewedProducts,'buyedProducts':buyedProducts})
    categories=Category.objects.all()
    return render(request,'index.html',{'categories':categories,'bestProducts':bestProducts,'newProducts':newProducts,'viewedProducts':viewedProducts,'buyedProducts':buyedProducts})
   

def loginUser(request):
    """
  This method takes to login page.



  :param name: request
  :type request: Implicit.
  :returns:  render -- index.html page according to if else conditions.

 .. note::
    This method shows viewed products also if successful login.
 """

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
            return render(request,'index.html',{'categories':categories,'message':'Incorrect Password','bestProducts':bestProducts,'newProducts':newProducts,'viewedProducts':viewedProducts,'buyedProducts':buyedProducts})
    if request.session.has_key('userName'):
        userName=request.session['userName']
        return render(request,'index.html',{'categories':categories,'userName':userName,'bestProducts':bestProducts,'newProducts':newProducts,'viewedProducts':viewedProducts,'buyedProducts':buyedProducts})
    return render(request,'index.html',{'categories':categories,'bestProducts':bestProducts,'newProducts':newProducts,'viewedProducts':viewedProducts,'buyedProducts':buyedProducts})

def logout(request):
    """
      This method controls the logout page.



     :param name: request
     :type request: Implicit.
     :returns:  render -- index.html page redirection.

    .. note::
       This method ends the current session.
    """

    del request.session['userName']
    del request.session['userEmail']
    return redirect("index")

def product(request,product_id):
    """
  This method controls the product page.


  :param name: request.
  :type request: Implicit.
  :param name: product_id.
  :type product_id: Integer.

  :returns:  render -- product.html page according to if else conditions.

 .. note::
    This method gets details of products from the **database**.
 """

    categories=Category.objects.all()
    product=Product.objects.get(id=product_id)
    product.productViewed=product.productViewed+1
    reviews=Review.objects.filter(reviewProduct=product).order_by('-reviewAddedDate')
    sameProducts=Product.objects.filter(productCategory=product.productCategory)
    product.save()
    if request.session.has_key('userName'):
        userName=request.session['userName']
        user=User.objects.get(userEmail=request.session['userEmail'])
        return render(request,"product.html",{'categories':categories,'product':product,'userName':userName,'myProducts':user.userProducts.all(),'sameProducts':sameProducts,'reviews':reviews})
    return render(request,"product.html",{'categories':categories,'product':product,'sameProducts':sameProducts,'reviews':reviews})
    

def getProductsCategory(request,selCategory):
    """
     This method controls the product_category page.


     :param name: request.
     :type request: Implicit.
     :param name: selCategory.
     :type selCategory: String.

     :returns:  render -- product_category.html page according to if else conditions.

    .. note::
       This method gets details of products from the **database**.
    """
    categories=Category.objects.all()
    products=Product.objects.filter(productCategory=Category.objects.get(categoryName=selCategory))
    print(products)
    if request.session.has_key('userName'):
        userName=request.session['userName']
        return render(request,"product_category.html",{'products':products,'categories':categories,'selCategory':selCategory,'userName':userName})
    return render(request,"product_category.html",{'products':products,'categories':categories,'selCategory':selCategory})

def search(request):
    """
  This method controls the product_search page.


  :param name: request.
  :type request: Implicit.


  :returns:  render -- product_search.html page.

 .. note::
    This method gets details of products from the **database**.
 """

    searchString=request.GET['search']
    categories=Category.objects.all()
    products=Product.objects.filter(productName__icontains=searchString)
    if request.session.has_key('userName'):
        userName=request.session['userName']
        return render(request,"product_search.html",{'products':products,'categories':categories,'searchString':searchString,'userName':userName})
    return render(request,"product_search.html",{'products':products,'categories':categories,'searchString':searchString})


def myProducts(request):
    """
     This method controls the my_products page.


     :param name: request.
     :type request: Implicit.


     :returns:  render --my_products.html page.

    .. note::
       This method gets details of user,products from the **database**.
    """
    user=User.objects.get(userEmail=request.session['userEmail'])
    categories=Category.objects.all()
    if request.session.has_key('userName'):
        userName=request.session['userName']
        return render(request,'my_products.html',{'categories':categories,'userName':userName,'products':user.userProducts.all()})
    return render(request,'my_products.html',{'categories':categories,'products':user.userProducts.all()})


def myCart(request):
    """
     This method controls the my_cart page.


     :param name: request.
     :type request: Implicit.


     :returns:  render --my_cart.html page.
    .. note::
       This method gets details of products from the **database**.
    """
    user=User.objects.get(userEmail=request.session['userEmail'])
    categories=Category.objects.all()
    price=0
    for product in user.userCart.all():
        price+=product.productDiscountedPrice
    if request.session.has_key('userName'):
        userName=request.session['userName']
        return render(request,'my_cart.html',{'categories':categories,'userName':userName,'products':user.userCart.all(),'userAddress':user.userAddress,'totalPrice':price})
    return render(request,'my_cart.html',{'categories':categories,'products':user.userCart.all()})

def savefav(request,product_id):
    """
     This method saves the favorite products.


     :param name: request.
     :type request: Implicit.
     :param name: product_id.
     :type product_id: Integer.
     :returns:  redirect method

    .. note::
       This method gets details of products from the **database**.
    """
    product=Product.objects.get(id=product_id)
    user=User.objects.get(userEmail=request.session['userEmail'])
    user.userProducts.add(product)
    return redirect('product',product_id)

def removefav(request,product_id):
    """
     This method removes from  the favorite products.


     :param name: request.
     :type request: Implicit.
     :param name: product_id.
     :type product_id: Integer.

     :returns:  redirect method

    .. note::
       This method gets details of products from the **database**.
    """

    product=Product.objects.get(id=product_id)
    user=User.objects.get(userEmail=request.session['userEmail'])
    user.userProducts.remove(product)
    return redirect('product',product_id)

def addToCart(request,product_id):
    """
     This method adds item to Cart..


     :param name: request.
     :type request: Implicit.
     :param name: product_id.
     :type product_id: Integer.
     :returns:  redirect method

    .. note::
       This method gets details ofproducts from the **database**.
    """
    product=Product.objects.get(id=product_id)
    user=User.objects.get(userEmail=request.session['userEmail'])
    user.userCart.add(product)
    return redirect('product',product_id)


def buyedProducts(request):
    """
     This method for showing buyed or purchased products.


     :param name: request.
     :type request: Implicit.


     :returns:  render-- buyed_products.html page

    .. note::
       This method gets details of products from the **database**.
    """
    user=User.objects.get(userEmail=request.session['userEmail'])
    categories=Category.objects.all()
    if request.session.has_key('userName'):
        userName=request.session['userName']
        return render(request,'buyed_products.html',{'categories':categories,'userName':userName,'products':user.userBuyedProducts.all()})
    return render(request,'buyed_products.html',{'categories':categories,'products':user.userBuyedProducts.all()})

def removeCart(request,product_id):
    """
     This method removes product from  the Cart.


     :param name: request.
     :type request: Implicit.
     :param name: product_id.
     :type product_id: Integer.

     :returns:  redirect method

    .. note::
       This method gets details of user,products from the **database**.
    """
    product=Product.objects.get(id=product_id)
    user=User.objects.get(userEmail=request.session['userEmail'])
    user.userCart.remove(product)
    return redirect('myCart')

def give_review(request,product_id):
    """
     This method removes from  the favorite products.


     :param name: request.
     :type request: Implicit.
     :param name: product_id.
     :type product_id: Integer.

     :returns:  redirect method

    .. note::
       This method used to give stars to pruducts.
    """
    title=request.GET['title']
    desc=request.GET['description']
    star=int(request.GET['star'])
    rating=star*21
    product=Product.objects.get(id=product_id)
    preReview=product.avgReview*product.noOfReviews
    product.noOfReviews=product.noOfReviews+1
    product.avgReview=(preReview+rating)/product.noOfReviews
    product.save()
    user=User.objects.get(userEmail=request.session['userEmail'])
    review=Review(reviewTitle=title,reviewDesc=desc,reviewRating=rating,reviewUser=user,reviewProduct=product)
    review.save()
    return redirect('product',product_id)
def checkout(request,price):
    pass
