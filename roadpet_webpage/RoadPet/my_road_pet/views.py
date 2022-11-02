from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    # return HttpResponse('my_road_pet first page')
    return render(request, 'my_road_pet/index.html')