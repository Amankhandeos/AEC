from django.shortcuts import render,redirect
from jobs.models import Product_detail,Categorie


def labour(request,data):
        if request.session.get('username'):
                lab=Categorie.objects.get(name=data)
                print(lab)
                worker = Product_detail.objects.filter(category=lab.id)
                print(worker)
                for x in worker:
                        print(x.id, x.name)

                return render(request, "labour.html", {'labour': worker})
        else:
                return redirect("/login")






