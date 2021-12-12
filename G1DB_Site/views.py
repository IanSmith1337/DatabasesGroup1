from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.http.response import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.password_validation import validate_password
from pyrebase import *
from pyrebase.pyrebase import Database
from G1DB_Site.errors import *
from G1DB_Site.models import Customer, Employee, User, Order1, RankData



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
        if(direction == "login"):
            return render(request, "login.html")
        else:
            return render(request, "custHome.html") # Entrypoint
    else:
        currentUser = User.objects.get(uid=request.session["lid"])
        if(direction == "order"):
            return render(request, "order.html", {"name": currentUser.name})
        else:
            return render(request, "home.html", {"name": currentUser.name})
            
def entry(request):
    return redirect("home") ## Entrypoint

def home(request):
    return waterfall(request, None)

def order(request):
    return waterfall(request, "order")

def login(request):
    return waterfall(request, "login")

def signup(request):
    return waterfall(request, "signup")

def display404(request, exception):
    return render(request, "404.html", exception)

def display403(request, exception):
    return render(request, "403.html", exception)

def display400(request, exception):
    return render(request, "400.html", exception)

def display500(request):
    return render(request, "500.html")

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
    try:
        if email == None: 
            raise EmptyInputError("Email is required!")
        if password == "": 
            raise EmptyInputError("Password is required!")
        user = auth.sign_in_with_email_and_password(email, password)
        lid = user['localId']
        request.session['lid'] = lid
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
        userSave.email = email
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
    if(not request.session.__contains__("uid")):
        raise PermissionDenied()
    employees = Employee.objects.all()

    if request.method == 'POST':
        if request.POST.get('fname') and request.POST.get('lname'):
            post = Employee()
            post.fname = request.POST.get('fname')
            post.lname = request.POST.get('lname')
            post.save()

        return render(request, 'employee.html', {'employee':employees})

    else:
        return render(request, 'employee.html', {'employee':employees})

def createCustomer(request):
    if(not request.session.__contains__("uid")):
        raise PermissionDenied()
    customers = Customer.objects.all()

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

        return render(request, 'customer.html', {'customer':customers})

    else:
        return render(request, 'customer.html', {'customer':customers})
    
def handleOrder(request):
    if(not request.session.__contains__("uid")):
        raise PermissionDenied()
    if request.method=="POST": 
        if request.POST.get("amount") and request.POST.get("deliveryfee") and request.POST.get("tax") and request.POST.get("total"):
            order1 = Order1()
            order1.amount=request.POST.get('amount')
            order1.deliveryfee=request.POST.get('deliveryfee')
            order1.tax=request.POST.get('tax')
            order1.total_amount= request.POST.get('total')
            order1.save()
            
        if request.POST.get("zipcode"):
            rd = RankData()
            zipC = request.POST.get("zipcode")
            zipData = RankData.objects.get(zipcode=zipC)
            print(zipData)
            rank = zipData.rank
            return render(request, 'order.html', {"rank": rank})
        return render(request, 'order.html')
    else:
        return render(request, 'order.html')