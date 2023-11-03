from django.shortcuts import render, redirect

from frontent.models import registerdb
from kapp.models import categorydb, productdb


# Create your views here.

def homepage(req):
    cat = categorydb.objects.all()
    return render(req, "index2.html", {'cat': cat})




def aboutpage(req):
    return render(req, "aboutus.html")


def registerpage(req):
    return render(req, "register.html")


def saveregister(req):
    if req.method == "post":
        re = req.POST.get('username')
        rp = req.POST.get('password')
        obj = registerdb(username=re, rpassword=rp)
        obj.save()
        return redirect(homepage)


def login_page(req):
    return render(req, "register.html")


def login_user(request):
    if request.method == "post":
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        if registerdb.objects.filter(username=un, password=pwd).exists():
            un = request.POST.get['username'] = un
            pwd = request.POST.get['password'] = pwd
            return redirect(homepage)
        else:
            return redirect(login_page)
    return redirect(login_page)
def productpage(request):
    pro=productdb.objects.all()
    return render(request,"products.html",{'pro':pro})


def filterdpage(req,cat_name):
    data = productdb.objects.filter(catname=cat_name)
    return render(req,"filterd_pd_page.html",{'data':data})