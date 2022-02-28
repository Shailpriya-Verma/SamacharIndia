from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.
def home(request):
    # order_by('-id') will show data in descending order
    # [0:4] will show only four data from category
    CData=category.objects.all().order_by('-id')[0:4]
    ndata=news.objects.all().order_by('-id')[0:8]
    notidata=notification.objects.all().order_by('-id')[0:2]
    sdata=slider.objects.all().order_by('-id')[0:4]
    return render(request,'user/index.html',{'cD':CData,'nD':ndata,'noti':notidata,'sD':sdata})

def aboutus(request):
    return render(request,'user/aboutus.html')

def mynews(request):
    a=request.GET.get('msg')
    sdata=request.GET.get('search')
    # if value of a is not empty then show only clicked category news
    if a is not None:
        ndata = news.objects.filter(ncategory=a)
    # if value of a is empty then show all news

    # code start for search box
    elif sdata is not None:
        x=news.objects.filter(Q(nhead__icontains=sdata) |Q (ndes__icontains=sdata) )
        if len(x)>0:
            ndata=x;
        else:
            return HttpResponse("<script>alert('Data not Found....');window.location.href='/user/mynews'</script>")
    # code end for search box
    else:
        ndata = news.objects.all().order_by('-id')

    cdata=category.objects.all()



    return render(request,'user/news.html',{'cat':cdata,'n':ndata})

def contactus(request):
    status=False
    if request.method=='POST':
        Name=request.POST.get("name")
        Mobile = request.POST.get("mobile")
        Email = request.POST.get("email")
        Message = request.POST.get("msg")
        res=contact(name=Name,email=Email,mobile=Mobile,message=Message)
        res.save()
        status=True
    return render(request,'user/contactus.html',{'S':status})

def video(request):
    cdata = category.objects.all()
    a = request.GET.get('msg')

    # if value of a is not empty then show only clicked category news
    if a is not None:
        vdata = videonews.objects.filter(vcategory=a)
    # if value of a is empty then show all news
    else:
        vdata=videonews.objects.all().order_by('-id')

    return render(request,'user/video.html',{'cD':cdata,'vD':vdata})

def readmore(request):
    a=request.GET.get('msg') #here when function is call 'a' will get the value of msg
    ndata=news.objects.filter(id=a) #here readmore page show only those news on which button will be clicked
    return render(request,'user/readmore.html',{'RD':ndata})

