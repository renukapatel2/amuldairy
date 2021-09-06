from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # User side pages
   
    path('user-indexpage/',views.UserIndexPage,name="indexpage"),
    path('user-registerpage/',views.UserRegisterPage,name="register"),
    path('user-loginpage/',views.UserLoginPage,name="login"),
    path('user-forgetpass/',views.UserForgetPass,name="forgetpass"),
    path('user-logout/',views.Userlogout,name="logout"),
    path('',views.UserHomePage,name='homepage'),
    path('user-viewcart/',views.UserViewCart,name='viewcart'),
    path('contacts/',views.Contact,name='contacts'),
    path('user-order/',views.UserOrder,name='userorder'),

    # User side functions
    path('registeruser/',views.RegisterUser,name="registeruser"),
    path('loginuser/',views.LoginUser,name="loginuser"),
    path('user-enterotp/',views.UserEnterOTP,name="enterotp"),
    path('user-otpverify/',views.UserOTPVerify,name='otpverify'),
    path('user-changepassword/',views.UserChangePassword,name='changepassword'),
    path('user-checkout/',views.Checkout,name='checkout'),
    path('user-profile/',views.UserProfile,name='userprofile'),
    path('user-profileupdate/',views.UserProfileUpdate,name='userprofileupdate'),
    path('user-addtocart/<int:pk>',views.UserAddtoCart,name='useraddtocart'),
   
    path('UserRee/<int:pk>/',views.remove,name='remove'),

    # Seller side pages
    path('seller-registerpage/',views.SellerRegisterPage,name='s-register'),
    path('seller/',views.SellerLoginPage,name='s-login'),
    path('seller-indexpage/',views.SellerIndex,name='sellerindexpage'),
    path('seller-forgetpass/',views.SellerForgetPass,name='s-forgetpass'),
    path('seller-logout/',views.SellerLogout,name='s-logout'),
    path('seller-profile/',views.SellerProfile,name='profile'),
    path('seller-AddProductPage/',views.SelleraddProduct,name='addPro'),
    path('seller-Productadd/',views.SelleraddProd,name="productaddig"),
    path('seller-showproduct/',views.SellerShowProduct,name='showproduct'),
    path('seller-contact/',views.SellerContact,name="sellercontact"),
    path('confirm/',views.Confirm,name='confirm'),
    
   
    # Seller Side Functions
    path('seller-register/',views.SellerRegister,name="sregister"),
    path('seller-login/',views.SellerLogin,name='slogin'),
    path('seller-enterotp/',views.SellerEnterOTP,name='s-enterotp'),
    path('seller-otpverify/',views.SellerOTPVerify,name='s-otpverify'),
    path('seller-changepass/',views.SellerChangePassword,name='s-changepass'),
    path('seller-productdelete/<int:pk>/',views.SellerProductDelete,name='delete'),
    path('seller-updateprofile/',views.SellerProfileUpdate,name='s-updateprofile'),

    
]    
