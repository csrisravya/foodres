from email.mime import message
from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request,"authentication/index.html")

def signup(request):
    
    if request.method == "POST":
        # these below like are to take the user i/p to the backend
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if pass1 != pass2:
            return HttpResponse("Re confirm Your Password!")
            
        
        #now , after taing their infor, we are registering the user to the backed
        #hence we import the contrib library, and create a user object myuser
        if User.objects.filter(username = username).first():
             messages.error(request, "This username is already taken")
             return redirect('home')
        
        myuser = User.objects.create_user(username, email, pass1) #the username, email and password 
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False

        myuser.save() # all info is saved
        #messages is a library which is used to send messages after a certain action
        messages.success(request, "Your Account has been created succesfully!!")
        #as  soon as the user finishes signup, he is redirected to signin/login again
        return redirect('signin')
    #we need to make migrations before being able to save the details 
    
    return render(request,"authentication/signup1.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username'] #taking name of user
        pass1 = request.POST['pass1']
        
        #django will authenticate the entered username and password
        user = authenticate(request,username=username, password=pass1) #this may return a None/not None response
        #return None is user is NOT AUTHENTICATED 
        if user is not None:
            login(request, user) # user authenticated, hence login
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            #return render(request, "authentication/index.html",{"fname":fname}) #creating dictionary of firstname to send their greeting
            return render(request, 'authentication/aboutus.html')
        else:
            messages.error(request, "Bad Credentials!! Please Signup if credentials are right!")
            return redirect('home')
    return render(request,"authentication/signin.html")

def signout(request):
    # pass: will throw an error
    logout(request)
    return redirect("home")

def aboutus(request):
    return render(request,'authentication/aboutus.html')

def donor(request):
    return render(request,"authentication/donor.html")
#<a class="nav-link" href="{% url 'donor' %}">Doner</a>
def receiver(request):
    return render(request,"authentication/receiver.html")