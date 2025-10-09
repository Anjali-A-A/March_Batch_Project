from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.urls import reverse
# from django.contrib.auth.models import User

# Create your views here.
# def register(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password1')
#         confirm_password = request.POST.get('confirm_password')
#         if password != confirm_password:
#             messages.error(request, 'Passwords do not match.')
#             return redirect('accounts:register')
#         if User.objects.filter(username=username).exists():
#             messages.error(request, 'Username already exists.')
#             return redirect('accounts:register')
#         if User.objects.filter(email=email).exists():
#             messages.error(request, 'Email already exists.')
#             return redirect('accounts:register')
#         user = User.objects.create_user(username=username, email=email, password=password)
#         user.save()
#         messages.success(request, 'Registration successful. Please log in.')
#         return redirect('accounts:login')
#     return render(request, 'register.html')
        

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            return redirect('login')
        # else:
            # print("form errors:", form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
    
def login_view(request):
    if request.method == 'POST':
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # user = authenticate(request, username=username, password=password)
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('shop:allProdCat')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

        # if user is not None:
        #     login(request, user)
        #     messages.success(request, '{user.username} have successfully logged in.')   
        #     return redirect('shop:allProdCat') 
        # else:
        #     messages.error(request, 'Invalid username or password.')
        #     return redirect('accounts:login')
    # return render(request, 'login.html')

def logout_view(request):
    logout(request)
    # messages.success(request, 'You have successfully logged out.')
    return redirect('shop:allProdCat')

def profile_view(request):
    return render(request, 'profile.html')