from django.shortcuts import render
from .forms import PassengerRegForm
from .models import PassengerRegModel
from django.http import HttpResponse


def passengerReg(request):
    form = PassengerRegForm()
    if request.method =='POST':
        form = PassengerRegForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return render(request,"testapp/index.html",{"msg":"You are registered successfully"})
    return render(request,"testapp/index.html",{'dis':form})

def loginCheck(request):
    if request.method=='POST':
        uname = request.POST.get('uname')
        upass = request.POST.get('upass')
        pr = PassengerRegModel.objects.filter(username = uname, password = upass)
        if pr:
            return render(request,"testapp/welcomeuser.html", 
            {'Customer Name': pr.cname, 'Username':pr.username, 'Membership_type':pr.membership_type})
        else:
            return HttpResponse("nothing")
    return  render(request,"testapp/login.html",{"msg":"Please enter valid details"}) 





