from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cPassword = request.POST['cPassword']
        if password == cPassword:
            if User.objects.filter(username = username).exists():
                messages.info(request,"username exists")
                return redirect('register')

            if User.objects.filter(email = email).exists():
                messages.info(request,"email exists")
                return redirect('register')
            else:

                user = User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname, email=email)

                user.save();

        else:
            messages.info(request,'password not match')
            return redirect('register')
        return redirect('/')

    return render(request,'register.html')
