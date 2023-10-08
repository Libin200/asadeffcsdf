from django.shortcuts import render,redirect
from django.http import HttpResponse
from jayapp.models import abijith,saaa
from jayapp.form import abijithform,saaaform
from jayapp.function import file_upload
# Create your views here.
def index(request):
    if request.method=="POST":
        fff=abijithform(request.POST)
        if fff.is_valid():
            try:
                fff.save()
                return redirect('/view')
            except:
                fff=abijithform()
                return render(request,"aaa.html",{"form":fff})
        else:
            a="this no is already taken"
            fff=abijithform()
            return render(request,"aaa.html",{"form":fff,"a":a})
    else:
        fff=abijithform()
        return render(request,"aaa.html",{"form":fff})

def view(request):
    form=abijith.objects.all()
    return render(request,'view.html',{'form':form})

def edit(request,n):
    form=abijith.objects.get(id=n)
    return render(request,'update.html',{'form':form})

def update(request,n):
    form=abijith.objects.get(id=n)
    forms=abijithform(request.POST,instance=form)
    if forms.is_valid():
        forms.save()
        return redirect("/view")
    else:
        return render(request,'edit.html',{'form':form})
    
def destroy(request,n):
    form=abijith.objects.get(id=n)
    form.delete()
    return redirect("/view")

def upload(request):
    if request.method=="POST":
        fff=saaaform(request.POST)
       
        file_upload(request.FILES['f'])
        return HttpResponse("file uploaded successfully")
                
           

    else:
        fff=saaaform()
        return render(request,"ip.html",{"form":fff})
