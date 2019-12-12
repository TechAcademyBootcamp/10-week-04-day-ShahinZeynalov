from django.shortcuts import render

# Create your views here.



def index(request):
    context={
        'title':'It is my first task with django'
    }
    return render(request,'carousel/index.html',context)
