from django.shortcuts import render

# Create your views here.
def viewpets(request):
    return render(request,'generalmodule/viewpets.html')

def rateus(request):
    return render(request,'generalmodule/rateus.html')

def contactus(request):
    return render(request,'generalmodule/contactus.html')

def viewproducts(request):
    return render(request,'generalmodule/viewproducts.html')

def grooming_essentials(request):
    return render(request,'generalmodule/grooming_essentials.html')

def enrichmentactivites(request):
    return render(request,'generalmodule/enrichmentactivites.html')

def donate(request):
    return render(request,'generalmodule/donate.html')