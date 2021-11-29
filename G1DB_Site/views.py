from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth.password_validation import validate_password
from pyrebase import *
from pyrebase.pyrebase import Database
from G1DB_Site.errors import *
from G1DB_Site.models import Customer, Employee, User



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
currentUser = None

def waterfall(request, direction):
    global currentUser
    if(not request.session.__contains__("uid")):
        if(direction == "signup"):
            return render(request, "registration.html")
        else:
            return render(request, "login.html")
    else:
        currentUser = User.objects.get(uid=request.session["lid"])
        print(currentUser)
        return render(request, "home.html", {"name": currentUser.name})

def entry(request):
    return render(request, "login.html")

def home(request):
    return waterfall(request, "home")

def login(request):
    return waterfall(request, "login")

def signup(request):
    return waterfall(request, "signup")

def logout(request):
    global currentUser
    try:
        del request.session['uid']
        currentUser = None
    except:
        pass
    return redirect("login")

def handleLogin(request):
    global currentUser
    if(request.session.__contains__("uid")):
        return redirect("/home")
    email = request.POST.get("email")
    password = request.POST.get("password")
    print("retrieve success.")
    try:
        if email == None: 
            raise EmptyInputError("Email is required!")
        if password == "": 
            raise EmptyInputError("Password is required!")
        user = auth.sign_in_with_email_and_password(email, password)
        print("signin success.")
        lid = user['localId']
        request.session['lid'] = lid
        print("uid lookup success.")
        currentUser = User.objects.get(uid=lid)
    except ObjectDoesNotExist as e:
        message = "User doesn't exist. Please create an account. \nIf this is an error, check your email address and try again."
        if(message == ""):
            message = "Error:" + str(e)
        logMessage = str(e).replace("\n", ";--- ")
        print(logMessage)
        return render(request, "login.html", {"message":message})
    except Exception as e:
        message = "Error:" + str(e).replace("[", "").partition('"message":')[2].partition(",")[0].replace("'", "").replace('"', "")
        if(message == ""):
            message = "Error:" + str(e)
        logMessage = str(e).replace("\n", ";--- ")
        print(logMessage)
        return render(request, "login.html", {"message":message})
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return redirect("/home")

def handleSignUp(request):
    global currentUser
    if(request.session.__contains__("uid")):
        return redirect("/home")
    name = request.POST.get("name")
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        if email == None: 
            raise EmptyInputError("Email is required!")
        if password == "":
            raise EmptyInputError("Password is required!")
        validate_password(password)
        user = auth.create_user_with_email_and_password(email, password)
        userSave = User()
        lid = user['localId']
        request.session['lid'] = lid
        userSave.uid = lid
        userSave.name = name
        session_id=user['idToken']
        request.session['uid'] = session_id
        userSave.save()
        currentUser = User.objects.get(uid=lid)
        print(currentUser)
    except Exception as e:
        message = "Error:" + str(e).replace("[", "").partition('"message":')[2].partition(",")[0].replace("'", "").replace('"', "")
        if(message == ""):
            message = "Error:" + str(e)
        logMessage = str(e).replace("\n", ";--- ")
        print(logMessage)
        return render(request, "registration.html", {"message":message})
    return redirect("/home")

def createEmployee(request):
    if request.method == 'POST':
        if request.POST.get('fname') and request.POST.get('lname'):
            post = Employee()
            post.fname = request.POST.get('fname')
            post.lname = request.POST.get('lname')
            post.save()

        return render(request, 'Employee.html')

    else:
        return render(request, 'Employee.html')


def createCustomer(request):
    if request.method == 'POST':
        if request.POST.get('custname') and request.POST.get('address') and request.POST.get('city') and request.POST.get('state') and request.POST.get('zipcode') and request.POST.get('phone'):
            post = Customer()
            post.custname = request.POST.get('custname')
            post.address = request.POST.get('address')
            post.city = request.POST.get('city')
            post.state = request.POST.get('state')
            post.zipcode = request.POST.get('zipcode')
            post.phone = request.POST.get('phone')
            post.save()

        return render(request, 'CustomerPage.html')

    else:
        return render(request, 'CustomerPage.html')