from django.shortcuts import render
from .models import design,team

# Create your views here.
def demo(request):
    obj = design.objects.all()
    obj1 = team.objects.all()

    return render(request, 'index.html',{'res':obj,'people':obj1})
