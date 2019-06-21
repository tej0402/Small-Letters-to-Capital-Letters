from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'utilities/index.html',)

def output(request):
    if request.method == 'POST' : 
        text = request.POST['text']
        processed = "Converted Into Caps : ", text.upper()
        print(text)
    return HttpResponse(processed) 

   
    
    
