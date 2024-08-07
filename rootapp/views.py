from django.shortcuts import render, redirect

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
            return redirect('viewdata')
    return render(request,'submit.html',{'form':form})

def viewdata(request):
    info= LifeInsurance.objects.all()
    return render(request, 'read.html', {'info': info})

def deldata(request,id):
    data=LifeInsurance.objects.get(id=id)
    data.delete()
    return redirect('viewdata')

def update_data(request,id):
    data=LifeInsurance.objects.get(id=id)
    form=InsuranceForm(instance=data)
    if request.method == 'POST':
        data = InsuranceForm(request.POST,instance=data)
        if data.is_valid():
            data.save()
            return redirect('viewdata')
    return render(request, 'update.html', {'form': form})

