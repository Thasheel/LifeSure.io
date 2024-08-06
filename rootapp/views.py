from django.shortcuts import render

from root.forms import InsuranceForm


# Create your views here.
def home(request):
    return  render(request,'home.html')
def index(request):
    return  render(request,'index.html')


def dash(request):

    return render(request,'dash.html')
def submit(request):
    form = InsuranceForm()
    return render(request,'submit.html',{'form':form})
