from django.shortcuts import render,redirect
from BookAdminApp.models import Book,Category,Payment
from UserApp.models import UserInfo,MyCart,OrderMaster
from django.http import HttpResponse
from django.contrib import messages





# Create your views here.
def home(request):
    cats = Category.objects.all()
    books = Book.objects.all()
    return render(request,"master.html",{"cats":cats,"books":books})

def ShowBooks(request,id):
    cats = Category.objects.all()
    books = Book.objects.filter(category = id)
    return render(request,"master.html",{"cats":cats,"books":books})

def ViewDetails(request,id):
    cats = Category.objects.all()
    book = Book.objects.get(id = id)
    return render(request,"ViewDetails.html",{"cats":cats,"book":book})

def addToCart(request):
     #check if user has logged in 
    if("uname" in request.session):
         #Get user info
        user = UserInfo.objects.get(username = request.session["uname"])
         #get the cake information
        book_id = request.POST["cid"]
        book = Book.objects.get(id= book_id)
        qty = request.POST["qty"]
        try:
            item = MyCart.objects.get(user=user,book=book)
        except:
            
             cart = MyCart()
             cart.user = user
             cart.book = book
             cart.qty = qty
             cart.save()     #Added to cart
             messages.info(request, 'Item added successfully')
        else:
            #return HttpResponse("Item already in cart")
            messages.info(request, 'Item already in cart')
        return redirect(showCartItems)
    
    else:
        return redirect(Login)
    
def showCartItems(request):
    if(request.method=="GET"):
        
         #Fetch those records which were added by the particular user
        items = MyCart.objects.filter(user = request.session["uname"])
        total = 0
     
        for item in items:
            total +=item.qty*item.book.price

        request.session["total"] = total
        return render(request,"showAllCartItems.html",{"items":items})
    else:
        cart_id = request.POST["cart_id"]
        item = MyCart.objects.get(id=cart_id)
        action = request.POST["action"]
        if(action == "remove"):
            item.delete()
        else:
            qty = request.POST["qty"]
            item.qty = qty
            item.save()

        return redirect(showCartItems)
    

def MakePayment(request):
    if(request.method == "GET"):
        return render(request,"MakePayment.html",{})
    else:
        card_no = request.POST["card_no"]
        cvv = request.POST["cvv"]
        expiry = request.POST["expiry"]
        try:
            buyer = Payment.objects.get(card_no=card_no,cvv=cvv,expiry=expiry)
        except:
            return redirect(MakePayment)
        else:
            owner = Payment.objects.get(card_no='222',cvv='222',expiry='12/2026')
            print(owner)
            print(buyer)
            buyer.balance -= float(request.session["total"])
            owner.balance += float(request.session["total"])
            buyer.save()
            owner.save()

            myorder = OrderMaster()
            user = UserInfo.objects.get(username=request.session["uname"])
            myorder.user  = user
            myorder.amount = request.session["total"]
            items = MyCart.objects.filter(user=user)
            details = ""
            for item in items:
                details+= item.book.book_name+" "
                item.delete()

            myorder.details= details
            myorder.save()

            #delete all cart items

            return render(request, 'thankyou.html', {'user': user})
        
def myorders(request):
    if(request.method == "GET"):
        user = UserInfo.objects.get(username = request.session["uname"])   
        orders = OrderMaster.objects.filter(user =user)
        cats= Category.objects.all
        books =[]
        for order in orders:
            detail =order.details.split(",")
            for item in detail:
                item_detail= item.split("-")
                id =item_detail[0]
                if(id.isalnum( )):
                    books.append(Book.objects.get(id=int(id)))
       # myorders.save()
        return render(request, 'orders.html', {'orders': orders,"books":books,"cats":cats,"user":user})
    else:
        request.session.clear()
        return redirect(home) 
        

       
def thankyou(request):
     #delete the session
    request.session.clear()
    return redirect(home)     
    
   


def SignOut(request):
    #Delete the session 
    request.session.clear()
    return redirect(home)

def Login(request):
    if(request.method=="GET"):
        return render(request,"Login.html",{})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        try:
            #Is user already present
            user = UserInfo.objects.get(username=uname,password=pwd)            
        except:
           message= "Invalid crendatials, plz try again later !!"
           return render(request,"Login.html",{"message":message})
        else:
            #if Login is successful then we create session for that user
            request.session["uname"] = uname
            return redirect(home)
        

def SignUp(request):
    if(request.method=="GET"):
        return render(request,"SignUp.html",{})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        try:
            #Is user already present
            user = UserInfo.objects.get(username=uname)   # by this get method we are passing the 
            #parameter if the parameter already exist in that model it will not raise the error
            # if it raises the error this means that email is not present.         
        except:
            #We can create user, as user is not present
            user = UserInfo(uname,pwd)
            user.save()
            return redirect(home)
        else:
            message = "This user already exist"
            return render(request,"SignUp.html",{"message":message})
#To close the session for a user without logging them out, you can #
# clear or delete the session data on the server-side. 
#django provides simple way

