from django.shortcuts import render

# Create your views here.
def tees(request):
    return render(request,'tees.html')