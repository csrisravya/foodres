from email.mime import message
from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from authentication.models import Order,Restaurant

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
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_no = request.POST.get('phone_no')
        address = request.POST.get('address')
        landmark = request.POST.get('landmark')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        food_type = request.POST.get('food_type')
        fresh_food_available = request.POST.get('fresh_food_available', False)
        food_remains_available = request.POST.get('food_remains_available', False)
        fresh_food_capacity = request.POST.get('fresh_food_capacity', 0)
        food_remains_capacity = request.POST.get('food_remains_capacity', 0)
        description = request.POST.get('description', '')

        restaurant = Restaurant(name=name, phone_no=phone_no, address=address, landmark=landmark, city=city, state=state, pincode=pincode, food_type=food_type, fresh_food_available=fresh_food_available, food_remains_available=food_remains_available, fresh_food_capacity=fresh_food_capacity, food_remains_capacity=food_remains_capacity, description=description)
        restaurant.save()
        return redirect('aboutus')
    else:
        return render(request,"authentication/donor.html")
#<a class="nav-link" href="{% url 'donor' %}">Doner</a>

def receiver(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        landmark = request.POST['landmark']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']
        food_capacity_needed = request.POST['food_capacity_needed']
        food_preference = request.POST['food_preference']
        
        order = Order(
            name=name,
            phone_number=phone_number,
            address=address,
            landmark=landmark,
            city=city,
            state=state,
            pincode=pincode,
            food_capacity_needed=food_capacity_needed,
            food_preference=food_preference,
        )
        order.save()
        return redirect('aboutus')
    else:
        return render(request,"authentication/receiver.html")
    