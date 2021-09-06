from django.shortcuts import render,redirect
from .models import *
from random import *

from django.conf import settings
from django.core.mail import send_mail
# import razorpay
# Create your views here.
# User

def UserIndexPage(request): 
    return render(request,"app/index.html")
    
def UserRegisterPage(request):
    return render(request,"app/register.html")

def UserLoginPage(request):
    return render(request,"app/login.html")

def UserHomePage(request):
    por = Productss.objects.all()
    return render(request,"app/home.html",{'data':por})

def UserForgetPass(request):
    return render(request,"app/forgetpass.html")

def UserViewCart(request):
    if 'id' in request.session:
        uid = User.objects.get(id=request.session['id']) 
        ca = Carts.objects.filter(Userid=request.session['id'])
        print("CArt----->",ca,request.session['id'])
        return render(request,"app/viewcart.html",{'ca':ca})
    else:
        return redirect("homepage")

def Checkout(request):
    if 'id' in request.session:
        return render(request,"app/checkout.html")
    else:
        return redirect("homepage")

def Contact(request):
    return render(request,"app/contacts.html")

def UserOrder(request):
    return render(request,"app/order.html")

def RegisterUser(request):
    if request.method == 'POST':
        fn= request.POST['fname']
        ln= request.POST['lname']
        addr=request.POST['adr']
        mob=request.POST['ph']
        em= request.POST['Email']
        pwd= request.POST['Password']


        slr = User.objects.create(Fname=fn,Lname=ln,Email=em,Mobile=mob,Address=addr,Password=pwd)
        
        return redirect("login")
    else:
        msg="Method Changes"
        return render(request,"app/register.html",{'err':msg})

def LoginUser(request):
    em=request.POST['Email']
    pwd=request.POST['Password']

    user = User.objects.filter(Email=em)

    if len(user) > 0:
        if user[0].Password == pwd:
            request.session['id'] = user[0].id
            request.session['Email'] = user[0].Email
            request.session['fname'] = user[0].Fname


            return redirect("indexpage")
        else:
            msg="Password is incorrect"
            return render(request,"app/login.html",{'err':msg})

    else:
        msg = "User Doesn't Found"
        return render(request,"app/login.html",{'err':msg})

def Userlogout(request):
    del request.session['id'] 
    del request.session['Email']
    del request.session['fname']
    return redirect("login")



def UserEnterOTP(request):
    if request.method=='POST':
        emailid=request.POST["Email"]
        user=User.objects.filter(Email=emailid)
        if len(user)>0:
            did=User.objects.get(Email=emailid)
            subject = 'Password Forgot'
            otp=""
            for i in range(6):
                otp+=str(randint(1,9))
            did.OTP =otp
            did.save()
            
            message = f"your otp is {otp}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [emailid, ]
            send_mail( subject, message, email_from, recipient_list )
            return render(request,"app/forgetpassotp.html",{'did':did})
        else:
            err="Incorrect Email Id"
            return render(request,"app/forgetpass.html")
    else:
        return render(request,"app/forgetpass.html")

def UserOTPVerify(request):
    if request.method=="POST":
        emailid=request.POST['Email']
        otp2=request.POST['otp']
        did=User.objects.get(Email=emailid)
        if did.OTP==int(otp2):
            return render(request,"app/Changepass.html",{"data":did})
        else:
            err="Incorect OTP"
            return render(request,"app/forgetpassotp.html",{'msg':err})


def UserChangePassword(request):
    if request.method=="POST":
        emailid=request.POST['Email']
        newpswd=request.POST["newpswd"]
        repeatpswd=request.POST["repeatpswd"]
        did=User.objects.get(Email=emailid)
        if newpswd == repeatpswd:
            did.Password = repeatpswd
            did.save()
            return render(request,"app/login.html")
    else:
        return render(request,"app/forgetpassotp.html")



def UserProfile(request):
    if 'id' in request.session:
        usr = User.objects.get(id=request.session['id'])
        return render(request,"app/userprofile.html",{'user':usr})
    else:
        return redirect('login')

def UserProfileUpdate(request):
    pro = User.objects.get(id=request.session['id'])
    pro.Fname = request.POST['fname'] if request.POST['fname'] else pro.Fname
    pro.Lname = request.POST['lname'] if request.POST['lname'] else pro.Lname
    pro.Email = request.POST['email'] if request.POST['email'] else pro.Email
    pro.Mobile = request.POST['ph'] if request.POST['ph'] else pro.Mobile
    pro.Address = request.POST['adr'] if request.POST['adr'] else pro.Address

    pro.save()
    return redirect("login")

def UserAddtoCart(request,pk):
    if 'id' in request.session:
        data= Productss.objects.get(id=pk)
        usr= User.objects.get(id=request.session['id'])

        crt= Carts.objects.create(product=data,Userid=usr)

        return redirect('homepage')
    else:
        return redirect('login')

def userproductDelete(request,pk):
    pro = Carts.objects.get(id=pk)
    pro.delete()
    return redirect("viewcart")

def remove(request,pk):
    if 'id' in request.session:
        cat = Carts.objects.get(id=pk)
        cat.delete()
        return redirect("viewcart")
    else:
        return redirect('homepage') 




## Seller side ##

def SellerRegisterPage(request):
    return render(request,"app/s-register.html")

def SellerLoginPage(request):
    return render(request,"app/s-login.html")

def SellerIndex(request):
    if 'sid' in request.session:
        return render(request,"app/s-indexpage.html")
    else:
        return redirect("s-login")    

def SelleraddProduct(request):
    if 'sid' in request.session:
        return render(request,"app/addproduct.html")
    else:
        return redirect("s-login")

def SellerForgetPass(request):
    return render(request,"app/s-forgetpass.html")


def SellerShowProduct(request):
    products = Productss.objects.all()
    return render(request,"app/showproduct.html",{'data':products})

def SellerContact(request):
    return render(request,"app/sellercontact.html")

def Confirm(request):
    return render(request,"app/confirm.html")

def SellerRegister(request):
    if request.method == 'POST':
        fn= request.POST['fname']
        ln= request.POST['lname']
        addr=request.POST['adr']
        mob=request.POST['ph']
        em= request.POST['Email']
        pwd= request.POST['Password']


        slr = Seller.objects.create(Fname=fn,Lname=ln,Email=em,Mobile=mob,Address=addr,Password=pwd)
        
        return redirect("s-login")
    else:
        msg="Method Changes"
        return render(request,"app/s-register.html",{'err':msg})

def SellerLogin(request):
    em=request.POST['Email']
    pwd=request.POST['Password']

    user = Seller.objects.filter(Email=em)

    if len(user) > 0:
        if user[0].Password == pwd:
            request.session['sid'] = user[0].id
            request.session['Email'] = user[0].Email
            request.session['fname'] = user[0].Fname


            return redirect("sellerindexpage")
        else:
            msg="Password is incorrect"
            return render(request,"app/s-login.html",{'err':msg})

    else:
        msg = "User Doesn't Found"
        return render(request,"app/s-login.html",{'err':msg})

def SellerEnterOTP(request):
    if request.method=='POST':
        emailid=request.POST["Email"]
        user=Seller.objects.filter(Email=emailid)
        if len(user)>0:
            did=Seller.objects.get(Email=emailid)
            subject = 'Password Forgot'
            otp=""
            for i in range(6):
                otp+=str(randint(1,9))
            did.OTP =otp
            did.save()
            
            message = f"your otp is {otp}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [emailid, ]
            send_mail( subject, message, email_from, recipient_list )
            return render(request,"app/s-forgetpassotp.html",{'did':did})
        else:
            err="Incorrect Email Id"
            return render(request,"app/s-forgetpass.html")
    else:
        return render(request,"app/s-forgetpass.html")

def SellerOTPVerify(request):
    if request.method=="POST":
        emailid=request.POST['Email']
        otp2=request.POST['otp']
        did=Seller.objects.get(Email=emailid)
        if did.OTP==int(otp2):
            return render(request,"app/s-Changepass.html",{"data":did})
        else:
            err="Incorect OTP"
            return render(request,"app/s-forgetpassotp.html",{'msg':err})



def SellerChangePassword(request):
    if request.method=="POST":
        emailid=request.POST['Email']
        newpswd=request.POST["newpswd"]
        repeatpswd=request.POST["repeatpswd"]
        did=Seller.objects.get(Email=emailid)
        if newpswd == repeatpswd:
            did.Password = repeatpswd
            did.save()
            return render(request,"app/s-login.html")
    else:
        return render(request,"app/s-forgetpassotp.html")

def SellerLogout(request):
    del request.session['sid'] 
    del request.session['Email']
    del request.session['fname']
    return redirect("s-login")

def SellerProfile(request):
    if 'sid' in request.session:
        usr = Seller.objects.get(id=request.session['sid'])
        return render(request,"app/sellerprofile.html",{'sel':usr})
    else:
        return redirect('s-login')

def SellerProfileUpdate(request):
    if 'sid' in request.session:
        pro = Seller.objects.get(id=request.session['sid'])
        pro.Fname = request.POST['fname'] if request.POST['fname'] else pro.Fname
        pro.Lname = request.POST['lname'] if request.POST['lname'] else pro.Lname
        pro.Email = request.POST['email'] if request.POST['email'] else pro.Email
        pro.Mobile = request.POST['ph'] if request.POST['ph'] else pro.Mobile
        pro.Address = request.POST['adr'] if request.POST['adr'] else pro.Address
            
        pro.save()
        return redirect("s-login")
    else:
        return redirect("s-updateprofile")
    

def SelleraddProd(request):
    if request.method == 'POST':
        pname = request.POST['Pname']
        pimg = request.FILES['Pro_img']
        pcat = request.POST['Pcat']
        pprice = float(request.POST['productprice'])
        pweight = request.POST['productweight'] 
        pweightcat = request.POST['prodweightcat']
        sellr= Seller.objects.get(id=request.session['sid'])
        cat=Category.objects.get(pcategory=pcat)
        print(f"{pname}     {cat}      {pprice}        {pweight}")
        pro = Productss.objects.create(Pro_name=pname,Pro_image=pimg,Pro_category=cat,Pro_price=pprice,Pro_weight=pweight,Pro_weightCat=pweightcat,sellerid=sellr)
        return redirect("showproduct")
    else:
        return render(request,"app/addproduct.html")  

def SellerProductDelete(request,pk):
    pro = Productss.objects.get(id=pk)
    pro.delete()
    return redirect("showproduct")






























        


