from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from .models import PetBooking
from .models import PetReturnRequest
from django.contrib import messages
# Create your views here.

def Logout(request):
    auth.logout(request)
    return redirect(request,'adminmodule/projecthomepage.html')

def success_page(request):
    return render(request, 'usermodule/success_page.html')
def returnandrequest(request):
    if request.method == 'POST':
        pet_id = request.POST['pet_id']
        pet_name = request.POST['pet_name']
        pet_breed = request.POST['pet_breed']
        pet_age = request.POST['pet_age']
        return_reason = request.POST['return_reason']
        return_date = request.POST['return_date']

        # Create a new PetReturnRequest object and save it to the database
        new_request = PetReturnRequest(
            pet_id=pet_id,
            pet_name=pet_name,
            pet_breed=pet_breed,
            pet_age=pet_age,
            return_reason=return_reason,
            return_date=return_date
        )
        new_request.save()

        return redirect('success_page')  # Redirect to a success page
        # Redirect to a success page
    else:
        return render(request, 'usermodule/returnandrequest.html')
def petmanagement(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        reason = request.POST['reason']
        pet_type = request.POST['pet_type']
        price = request.POST['price']

        mes = PetBooking.objects.create(name=name, email=email, reason=reason, pet_type=pet_type, price=price)
        mes.save()
        return HttpResponse("<h1 align='center'>Booked Sucessfully</h1> ")

    return render(request,'usermodule/petmanagement.html')

def articles(request):
    return render(request,'usermodule/articles.html')