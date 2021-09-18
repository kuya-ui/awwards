from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
@login_required(login_url = '/accounts/login/')
def index(request):