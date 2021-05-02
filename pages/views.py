from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    print(args,kwargs)
    print(request.user)
    return  render(request,"home.html",{}) # string of HTML code 

def contact_view(request, *args, **kwargs):
    return render(request,"contact.html",{} )


def about_view(request ,*args, **kwargs):
    my_context = {
        "my_text" : "This is about me",
        "my _number" :  123,
        "this_is_true" :True,
        "my_list" : [123, 4243, 12312, 321,"ABC"]
    }
    return render(request,'about.html',my_context)





