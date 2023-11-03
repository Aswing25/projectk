from django.shortcuts import render, redirect
from kapp.models import employedb, studentdb, categorydb, productdb


# Create your views here.

def indexpage(req):
    return render(req, "index.html")


def studentpage(req):
    return render(req, "add_student.html")


def employepage(req):
    return render(req, "employe.html")


def employesave(req):
    if req.method == "POST":
        na = req.POST.get('name')
        ag = req.POST.get('age')
        mb = req.POST.get('mobile')
        em = req.POST.get('email')
        cm = req.POST.get('company')
        sal = req.POST.get('salary')
        add = req.POST.get('address')
        obj = employedb(ename=na, eage=ag, mobile=mb, email=em, company=cm, salary=sal, address=add)
        obj.save()
        return redirect(employepage)


def studentsave(req):
    if req.method == "POST":
        fn = req.POST.get('name')
        ln = req.POST.get('email')
        em = req.POST.get('semail')
        obj = studentdb(sfname=fn, slname=ln, semail=em)
        obj.save()
        return redirect(studentpage)


def displayemploy(req):
    data = employedb.objects.all()
    return render(req, "displayemploye.html", {'data': data})


def displaystudent(req):
    data = studentdb.objects.all()
    return render(req, "displaystudent.html", {'data': data})


def categorypage(req):
    return render(req, "addcategory.html")


def categorysave(req):
    if req.method == "POST":
        cn = req.POST.get('cname')
        cd = req.POST.get('cdescription')
        cp = req.POST.get('cprice')
        cm = req.FILES['cimage']
        obj = categorydb(name=cn, Cdes=cd, categoryimg=cm, cprice=cp)
        obj.save()
        return redirect("categorypage")


def displaycategory(request):
    data = categorydb.objects.all()
    return render(request, "displaycategory.html", {'data': data})


def edit_category(request,dataid):
    category = categorydb.objects.get(id=dataid)
    cat=categorydb.objects.all()
    return render(request,"editcategory.html",{'category':category,'cat':cat})



def delete_category(req,dataid):
    data=categorydb.objects.get(id=dataid)
    data.delete()
    return redirect(displaycategory)


def update_categorydata(request,dataid):
    if request.method =="POST":
        cn = request.POST.get('cname')
        cd = request.POST.get('cdescription')
        cp = request.POST.get('cprice')
        categorydb.objects.filter(id=dataid).update(name=cn,Cdes=cd,cprice=cp)
        return redirect(displaycategory)


def addproductpage(req):
    data = categorydb.objects.all
    return render(req, "addproduct.html", {'data': data})


def productsave(req):
    if req.method == "POST":
        pn = req.POST.get('pname')
        cn = req.POST.get('cname')
        pd = req.POST.get('pdescription')
        pp = req.POST.get('pprice')
        pm = req.FILES['pimage']
        obj = productdb(productname=pn, description=pd, productimage=pm, price=pp, catname=cn)
        obj.save()
        return redirect("addproductpage")


def displayproduct(req):
    cat = productdb.objects.all()
    return render(req, "displayproduct.html", {'cat': cat})


def edit_product(req,productid):
    product = productdb.objects.get(id=productid)
    return render(req,"edit_product.html",{'product':product})


