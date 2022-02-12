from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from .models import FileUpload
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    
    else:
        return render(request, 'login.html')
    return render(request, 'index.html')

    

def loginuser(request):

    username = (request.POST.get('username'))
    password = (request.POST.get('password'))


    user = authenticate(username=username, password=password)
    if user is not None:
        print("Succesfully login")
        login(request, user)
        return render(request, 'index.html')
    # A backend authenticated the credentials
    else:
        print("Authentication failed")
    # No backend authenticated the credentials
  
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)

    return render(request, 'login.html')

def upload(request):
    if(request.method == 'POST'):
        file2 = request.FILES['file']
        document = FileUpload.objects.create(file=file2)
        document.save()
        return HttpResponse("Your file has been saved")
    return render(request, 'upload.html')