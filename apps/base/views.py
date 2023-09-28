from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    return redirect('home/')