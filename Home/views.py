from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from Home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt


#signup function
def signup(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exits")
            return redirect('signup')
        
        user=User.objects.create_user(username,email,password)
        user.save()
        messages.success(request,"Account created successfully!")
        return redirect("login")
    
    return render(request, "signup.html")

#login function 
@csrf_exempt
def user_login(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request,username=username, password=password)
        
        if user is not None:
            login (request,user)
            messages.success(request,"Logged in Successfully")
            return redirect("/")
        else:
            messages.error(request,"Invalid credentials")

    return render(request,'login.html')

#Logout Function
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('/')

# just for learning 
# Create your views here.
def index(request):
   #return HttpResponse("This is HomePage")
   context = {
    'variable1' : 'Emaan is Great', 
    'variable2' : 'Dua is Great' 
   }
   
   return render(request, "index.html")

def about(request):
    #return HttpResponse("This is AboutPage")
    return render(request, "about.html")
def services (request):
    #return HttpResponse("This is ServicesPage")
    return render(request, "services.html",)
def contact (request):
    #return HttpResponse("This is ContactsPage")
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        message= request.POST.get('message')
        contact= Contact(user=request.user,name=name, email=email, phone=phone, message=message)
        contact.save()
        messages.success(request, "Your message has been sent!")
    return render(request, "contact.html")