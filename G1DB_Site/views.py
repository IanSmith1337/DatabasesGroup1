from django.contrib.auth.password_validation import MinimumLengthValidator, get_password_validators
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.password_validation import validate_password
from pyrebase import *
from pyrebase.pyrebase import Database

from G1DB_Site.errors import *



config = {
  "apiKey": "AIzaSyCp1dOGmQo8v1gzkktKhxgzg7poFsXvMDI",
  "authDomain": "g1database.firebaseapp.com",
  "databaseURL": "https://g1database-default-rtdb.firebaseio.com/",
  "storageBucket": "g1database.appspot.com"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()
auth = firebase.auth()
message = None
logMessage = None

def waterfall(request, direction):
    print(request.session.__contains__("uid"))
    if(not request.session.__contains__("uid")):
        if(direction == "signup"):
            return render(request, "registration.html", {"message":message, "logMessage":logMessage})
        else:
            return render(request, "login.html", {"message":message, "logMessage":logMessage})
    else:
        return render(request, "home.html")

def entry(request):
    return render(request, "login.html")

def home(request):
    return waterfall(request, "home")

def login(request):
    return waterfall(request, "login")

def signup(request):
    return waterfall(request, "signup")

def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return redirect("login")

def handleLogin(request):
    if(request.session.__contains__("uid")):
        return redirect("/home")
    email = request.POST.get("email")
    password = request.POST.get("password")
    try:
        if email == None: 
            raise EmptyInputError("Email is required!")
        if password == "": 
            raise EmptyInputError("Password is required!")
        user = auth.sign_in_with_email_and_password(email, password)
        print(user)
    except Exception as e:
        message = str(e)
        logMessage = str(e).replace("\n", "!n!")
        return render(request, "login.html", {"message":message, "logMessage":logMessage})
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return redirect("/home")

def handleSignUp(request):
    if(request.session.__contains__("uid")):
        return redirect("/home")
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        if email == None: 
            raise EmptyInputError("Email is required!")
        if password == "":
            raise EmptyInputError("Password is required!")
        validate_password(password)
        user = auth.create_user_with_email_and_password(email, password)
        uid = user['localId']
        request.session['uid'] = uid
        print(user)
    except Exception as e:
        message = str(e).replace("['", "").replace("']", "")
        logMessage = str(e).replace("\n", "!n!").replace("['", "").replace("']", "")
        return render(request, "registration.html", {"message":message, "logMessage":logMessage})
    return redirect("/home")
