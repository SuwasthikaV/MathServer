from django.shortcuts import render 
def Vehicle(request):
    distance=float(request.POST.get('distance',0))
    fuelconsumed=float(request.POST.get('fuelconsumed',0))
    mileage=distance/fuelconsumed if request.method=='POST' else 0
    print("Distance_Travelled(in km):",distance)
    print("Amount_Of_Fuel(in litre):",fuelconsumed)
    print("Vehicle's_Mileage:",mileage)
    return render(request,'mathapp/math.html',{'distance':distance,'fuelconsumed':fuelconsumed,'mileage':mileage})