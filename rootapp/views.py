from django.shortcuts import render

from root.forms import InsuranceForm
from rootapp.models import LifeInsurance


# Create your views here.
def home(request):
    return  render(request,'home.html')
def index(request):
    return  render(request,'index.html')


def dash(request):

    return render(request,'dash.html')
def submit(request):
    form = InsuranceForm()
    if request.method == 'POST':
        data=InsuranceForm(request.POST)
        if data.is_valid():
            data.save()
    return render(request,'submit.html',{'form':form})

def viewdata(request):
    info= LifeInsurance.objects.all()
    return render(request, 'read.html', {'info': info})

