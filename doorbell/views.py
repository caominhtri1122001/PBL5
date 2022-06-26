from django.shortcuts import render
from matplotlib import image
import pyrebase
from .models import *

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
    # name = database.child('IMG').child('Manual_2022-06-26T02:24:28Z').child('downloadURL').get().val()
    all = database.child('IMG').get().val()
    print(type(all))
    list = []
    for key, value in all.items():
        print(key, value)
        print(value['downloadURL'])
        cc = GuestImage(name=key, image=value['downloadURL'], date=value['time'])
        list.append(cc)
    context = {
        'list':list,
    }
    return render(request, 'index.html', context)