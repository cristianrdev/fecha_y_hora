from django.shortcuts import render
from datetime import datetime

# Create your views here.
from django.shortcuts import render, HttpResponse
def index(request):
    context = {
        "fecha": datetime.now().strftime("%b %d, %Y"), 
        "hora": datetime.now().strftime("%H:%M %p")
    }
    return render(request,'index.html', context)
