from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    print(args,kwargs)
    print(request.user)
    return  render(request,"home.html",{}) # string of HTML code 

def contact_view(request, *args, **kwargs):
    return render(request,"contact.html" )


def about_view(request ,*args, **kwargs):
    return render(request,'about.html')





