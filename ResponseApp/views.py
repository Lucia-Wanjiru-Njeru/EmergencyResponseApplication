from django.shortcuts import render #Used to render HTML templates and return them as HTTP responses.
import json 
from django.http import JsonResponse
from .models import *
import indexmeter
from indexmeter.models import Emergencies

# Create your views here.

# View function for the index page
def index(request):
    # Render the "home_main_content.html" template and return it as an HTTP response
    return render(request,"home/home_main_content.html")
# View function for the emergencies page
def emergencies(request):

    


    # Render the "emergencies.html" template and return it as an HTTP response
    return render(request,"home/emergencies.html")

def ongoingEmergencies(request):
    # Render the "emergencies.html" template and return it as an HTTP response
    return render(request,"home/ongoing_summary.html")

def dataRetriever(request):
    if request.method == 'POST':
      
       data = json.loads(request.body).get('data')
       x_coords =json.loads(request.body).get('coordinates_x')
       y_coords =json.loads(request.body).get('coordinates_y')
       name =json.loads(request.body).get('name')
       type = json.loads(request.body).get('type')
       print(type)
       print(x_coords,y_coords,name)
       def save_emergencies_to_database(user,x_coords, y_coords,name,type):
            if x_coords is not None and y_coords is not None and type is not None:
                # Create a new Coordinates instance
                new_emergency = Emergencies()
                new_emergency.user = user
                new_emergency.lat = x_coords
                new_emergency.lon = y_coords
                new_emergency.location = name 
                new_emergency.emergency = type 

                # Save the new instance to the database
                new_emergency.save()
       def save_coordinates_to_database(x_coords, y_coords,name):
            if x_coords is not None and y_coords is not None:
                # Create a new Coordinates instance
                new_coordinates = Coordinates()
                new_coordinates.x_coordinate = x_coords
                new_coordinates.y_coordinate = y_coords
                new_coordinates.name = name 

                # Save the new instance to the database
                new_coordinates.save()
       save_coordinates_to_database(x_coords, y_coords,name)   
       save_emergencies_to_database(request.user,x_coords,y_coords,name,type)     
       return JsonResponse({'data':data},safe=False)
    return render(request,"collectorapp/collector.html")


