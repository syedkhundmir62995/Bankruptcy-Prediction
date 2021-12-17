from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
import joblib

def home(request):
    return render(request,'firstapp/home.html')


def login(request):

    if request.method == 'POST':
        uname = request.POST['uname']
        pass1 = request.POST['pass1']

        user = auth.authenticate(username = uname, password = pass1)

        if user:
            auth.login(request,user)
            return redirect('homepage')
        else:
            messages.warning(request,"Invalid Credentials")
            return redirect('loginpage')
    else:
        return render(request,'firstapp/login.html')

def logout(request):
    auth.logout(request)
    return redirect('homepage')

def signup(request):

    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        mail = request.POST['mail']
        uname = request.POST['uname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(username = uname).exists():
                print("Username already taken")
                messages.warning(request,"USERNAME ALREADY TAKEN")
                return redirect('signuppage')
            
            elif User.objects.filter(email = mail).exists():
                print("Email already exist")
                messages.warning(request,"EMAIL ALREADY TAKEN")
                return redirect('signuppage')
            
            else:
                user = User.objects.create_user(username = uname, first_name = fname,last_name = lname,password = pass1,email = mail)
                user.save()
                messages.success(request,"SIGN UP SUCCESSFULL")
                return redirect("loginpage") 

        else:
            print("Passwords does not match")
            messages.error(request,'PASSWORD DOES NOT MATCH !')
            return redirect('signuppage')

    else:   
        return render(request,'firstapp/signup.html')


def predict(request):
    
    cls = joblib.load('randomforest.pkl')
    if request.method == 'POST':
        stl = request.POST['stl']
        lta = request.POST['lta']
        si = request.POST['si']
        tatl = request.POST['tatl']
        clcps = request.POST['clcps']
        icps = request.POST['icps']
        iss = request.POST['is']
        catl = request.POST['catl']
        sta = request.POST['sta']
        castl = request.POST['castl']
        tsta = request.POST['tsta']
        stlcps = request.POST['stlcps']
        tcts = request.POST['tcts']
        caill = request.POST['caill']
        wc = request.POST['wc']
        
        ans = cls.predict([[stl,lta,si,tatl,clcps,icps,iss,catl,sta,castl,tsta,stlcps,tcts,caill,wc]])
        result = ""

        if(ans[0] == 0):
            print("Company will not bankrupt")
            messages.success(request,"COMPANY WILL NOT BANKRUPT")
        else:
            print("Comapany will Bankrupt")
            messages.warning(request,'COMPANY WILL BANKRUPT !!')
        return redirect('homepage')
    else:
        return render(request,'firstapp/predict.html')




def about(request):
    return render(request,'firstapp/about.html')

