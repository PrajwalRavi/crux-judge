from django.shortcuts import render
from django.http import HttpResponse
from .models import Problem
#from .forms import SubmissionForm
# Create your views here.

def index(request):
	
	prob_list= Problem.objects.order_by("problem_id")	
	return render(request, "list.html", {"prob_list" : prob_list})

