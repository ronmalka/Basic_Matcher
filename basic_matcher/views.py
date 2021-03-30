from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Candidate, Skill, Job
from .utility.candidate_finder import Candidate_Finder

def index(request):
    latest_candidates = Candidate.objects.order_by('pk').reverse()[:5]
    latest_jobs = Job.objects.order_by('pk').reverse()[:5]
    context = {'latest_candidates' : latest_candidates , 'latest_jobs' : latest_jobs}
    return render(request, 'basic_matcher/index.html',context = context)

def find_candidate(request):
    job_id = request.GET['job_id']
    fit_candidates = Candidate_Finder.candidate_finder(job_id)
    context = {'fit_candidates' : fit_candidates}
    return render(request,'basic_matcher/results.html',context = context)   

   