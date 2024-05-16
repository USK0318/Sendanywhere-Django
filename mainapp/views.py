from django.shortcuts import render,redirect
from .forms import gameform
from django.contrib import messages
from .models import gamedata
import os,time,random

# Create your views here.
def display0(request):
    return render(request,'main.html')

def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File '{file_path}' deleted successfully.")
        else:
            print(f"File '{file_path}' does not exist.")
    except Exception as e:
        print(f"Error deleting file '{file_path}': {e}")


def delet(request, pk):
    data=gamedata.objects.get(id=pk)
    time.sleep(5)
    delete_file(data.data.path)
    data.delete()
    return redirect('main')

    

def display2(request):
    if request.method=="POST":
        a=request.POST['text_input']
        try:
            data=gamedata.objects.get(id=a)
        except Exception:
            messages.error(request,'Invalied Code')
            return render(request,'second.html',{'nom':1})
        return render(request,'second.html',{'a':data,'nom':2})
    return render(request,'second.html',{'nom':1})
    
    
def display(request):
    if request.method=="POST":
        while True:
            a=random.randint(1000,1100)
            try:
                x=gamedata.objects.get(id=a)
            except Exception:
                b=a
                break
        a=request.FILES['image']
        cod=b
        gamedata.objects.create(id=b,data=a)
        return render(request,'first.html',{'nom':1,'c':cod})
    return render(request,'first.html',{'nom':2})

