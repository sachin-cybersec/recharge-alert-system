from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from django.contrib import messages



def MainPage(request):
    return render(request, 'main.html')

def AirtelPlanPage(request):
    return render(request, 'airtelplan.html')

def jioplan(request):
    return render(request, 'jioplan.html')

def viplan(request):
    return render(request, 'viplan.html')

def netflixplan(request):
    return render(request , 'netflixplan.html')

def login(request):
    if request.method == 'POST':
        phoneno = request.POST.get('phone number')
        password = request.POST.get('password')
        user = authenticate( request,username=phoneno,password=password)
        if user is not None:            
            auth_login(request,user)
            # return redirect('main.html') 
            return redirect('main')   
        else:
            return HttpResponse("user name or pass word is incorrect !")

    return render(request , 'login.html')


def signup(request):
        if request.method == 'POST':
            phoneno = request.POST.get('phone number')
            createpass = request.POST.get('create-password')
            confirmpass = request.POST.get('confirm-password')
            if createpass != confirmpass:
                # return HttpResponse("your password is not matching!")
                return redirect('noottrecharge')
            else:
                my_user = User.objects.create_user(phoneno,createpass,confirmpass) 
                my_user.save()
                return redirect('login')                          
        return render(request , 'signup.html')

# def signup(request):
#     if request.method == 'POST':
#         phoneno = request.POST.get('phone number')  # Getting phone number
#         createpass = request.POST.get('create-password')
#         confirmpass = request.POST.get('confirm-password')

#         # Check if passwords match
#         if createpass != confirmpass:
#             messages.error(request, "Your passwords do not match!")
#             return redirect('signup')  # Redirect back to signup page
        
#         # Check if user already exists
#         if User.objects.filter(username=phoneno).exists():
#             messages.error(request, "User with this phone number already exists!")
#             return redirect('signup')

#         # Create a new user
#         my_user = User.objects.create_user(username=phoneno, password=createpass)
#         my_user.save()

#         messages.success(request, "Signup successful! Please log in.")
#         return redirect('login')  # Redirect to login page

#     return render(request, 'signup.html')



def disneyplan(request):
    return render(request , 'disneyplan.html')

def hotstarplan(request):
    return render(request , 'hotstarplan.html')

def nomobilerecharge(request):
    return render(request , 'nomobilerecharge.html')

def noottrecharge(request):
    return render(request , 'noottrecharge.html')

def countdown(request):
    return render(request, 'countdown.html')

def button_view(request):
    return render(request, 'button_page.html')
