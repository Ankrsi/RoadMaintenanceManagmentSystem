from audioop import add
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib import auth
from .models import ComplaintDataLocation,ComplaintDataManual
from django.views.decorators.cache import never_cache
from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def splashscreen(request):
    return render(request,'splashscreen.html')
def main(request):
    for l in ComplaintDataLocation.objects.raw("select 1 as id,count(status) as c from App_complaintdatalocation"):
        t=l.c
    m=ComplaintDataManual.objects.raw("select 1 as id,count(status) as c from App_complaintdatalocation where status='Completed'")
    for i in m:
        r=i.c
    for l in ComplaintDataLocation.objects.raw("select 1 as id,count(status) as c from App_complaintdatamanual"):
        t+=l.c
    m=ComplaintDataManual.objects.raw("select 1 as id,count(status) as c from App_complaintdatamanual where status='Completed'")
    for i in m:
        r+=i.c
    return render(request,'main.html',{'t':t,'r':r})

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def lform(request):
    if request.method == 'POST':
        name=request.POST.get("uname")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        image=request.FILES.get("imagefile")
        latlong=request.POST.get("demo")
        s1=ComplaintDataLocation(name=name,email=email,phone=phone,image=image,latlong=latlong,status="In Process")
        s1.save()
        data=ComplaintDataLocation.objects.all()
        return render(request,'thank_you.html',{'token':data.last().id})
    return render(request,'locform.html')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def mform(request):
    if request.method == 'POST':
        name=request.POST.get("uname")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        addr=request.POST.get("addr")
        city=request.POST.get("city")
        state=request.POST.get("state")
        zip=request.POST.get("zip")
        image=request.FILES.get("imagefile")
        s2=ComplaintDataManual(name=name,email=email,phone=phone,addr=addr,city=city,state=state,zip=zip,image=image,status="In Process")
        s2.save()
        data=ComplaintDataManual.objects.all()
        return render(request,'thank_you.html',{'token':data.last().id})
    return render(request,'manform.html')
def status(request):
    if request.method == 'POST':
        token=request.POST.get("token")
        try:
            data=ComplaintDataLocation.objects.get(id=token)
            return render(request,'status.html',{'dataloc':data})
        except:
            try:
                data=ComplaintDataManual.objects.get(id=token)
                return render(request,'status.html',{'dataman':data})
            except:
                return render(request,'status.html',{'error':"Data Not Found!"})
    return render(request,'status.html')
