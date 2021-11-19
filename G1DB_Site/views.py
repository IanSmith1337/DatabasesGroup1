from django.shortcuts import render
from pyrebase import *
from pyrebase.pyrebase import Database



config = {
  "apiKey": "AIzaSyCp1dOGmQo8v1gzkktKhxgzg7poFsXvMDI",
  "authDomain": "g1database.firebaseapp.com",
  "databaseURL": "https://g1database-default-rtdb.firebaseio.com/",
  "storageBucket": "g1database.appspot.com"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()
auth = firebase.auth()

def signIn(request):
    return render(request,"login.html")
def home(request):
    return render(request,"home.html")
def signUp(request):
    return render(request,"registration.html")

def handleLogin(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    try:
        user = auth.sign_in_with_email_and_password(email, password)
    except Exception as e:
        message = "Invalid Credentials, please re-enter."
        logMessage = str(e).replace("\n", "!n!")
        return render(request,"login.html",{"message":message, "logMessage":logMessage})
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request,"home.html",{"email":email})
 
def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,"login.html")
 

 
def handleSignUp(request):
    email = request.POST.get('email')
    password = request.POST.get('pass')
    name = request.POST.get('name')
    try:
        user = auth.create_user_with_email_and_password(email, password)
        uid = user['localId']
        idToken = request.session['uid']
        print(uid)
    except:
       return render(request, "registration.html")
    return render(request,"login.html")
