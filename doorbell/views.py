from django.http import JsonResponse
from django.shortcuts import redirect, render
from matplotlib import image
from matplotlib.style import context
import pyrebase
from .models import *
from django.contrib.auth.decorators import login_required

# Firebase config here.
config = {
    "apiKey": "AIzaSyDuv-fG1A-JTWsIoHb_nzZewifPMlM96Qs",
    "authDomain": "pbl5-30b43.firebaseapp.com",
    "databaseURL": "https://pbl5-30b43-default-rtdb.firebaseio.com",
    "projectId": "pbl5-30b43",
    "storageBucket": "pbl5-30b43.appspot.com",
    "messagingSenderId": "986740194013",
    "appId": "1:986740194013:web:8f48ab1890766100467934"
}

firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

# Create your views here.
def home_view(request):
    return render(request, 'index.html')

def contact_view(request):
    return render(request, 'contact.html')

def live_view(request):
    return render(request, 'live.html')

def manage_view(request):
    guestList = []
    keyword = request.GET.get('keyword')
    if keyword:
        guest = database.child('IMG').get().val()
        for key, value in guest.items():
            if (value['time'].split('T')[0] == keyword):
                result = GuestImage(name=key, image=value['downloadURL'], date=value['time'].split('T')[0], time=value['time'].split('T')[1][:-1], gender=value['gender'])
                guestList.append(result)
    else:
        guest = database.child('IMG').get().val()
        for key, value in guest.items():
            print(key, value)
            # print(value['downloadURL'])
            # print(value['time'].split('T')[0])
            # print(value['time'].split('T')[1][:-1])
            result = GuestImage(name=key, image=value['downloadURL'], date=value['time'].split('T')[0], time=value['time'].split('T')[1][:-1] ,gender=value['gender'])
            guestList.append(result)
        
    context = {
        'guestList':guestList,
    }
    return render(request, 'manage.html', context)

def delete_view(request, name):
    guest = database.child('IMG').child(name).get().val()
    print(guest['time'])
    if request.method == 'POST':
        database.child('IMG').child(name).remove()
        return redirect('/manage')
    context = {
        'guest':guest['downloadURL'],
        'name':name,
    }
    return render(request, 'delete.html', context)

def login_view(request):
    context = {
        
    }
    if request.method == "POST":
        user = request.POST['username']
        password = request.POST['password']
        try:
            guest = authe.sign_in_with_email_and_password(user, password)
            return redirect('home')
        except:
            context = {
                'error':'The password or email is incorrect.'
            }
    return render(request, 'login.html', context)

def register_view(request):
    context = {
        
    }
    if request.method == "POST":
        user = request.POST['username']
        password = request.POST['password']
        conPassword = request.POST['confirmPassword']
        if ( password == conPassword):
            guest = authe.create_user_with_email_and_password(user, password)
            return redirect('home')
        else:
            context = {
                'error':'The password does not match.'
            }
        
    return render(request, 'register.html', context)


def sensor_view(request):
    if request.method == "POST":
        if 'led' not in request.POST:
            led = 'off'
        else:
            led = request.POST['led']
        if 'ring' not in request.POST:
            ring = 'off'
        else:
            ring = request.POST['ring']
        if 'sensor' not in request.POST:
            sensor = 'off'
        else:
            sensor = request.POST['sensor']
        print(led,ring,sensor)
        
        data = [{'led':led, 'ring':ring, 'sensor':sensor}]
        return JsonResponse(data, safe=False)
    return render(request, 'sensor.html')