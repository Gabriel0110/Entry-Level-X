from django.shortcuts import render
from job_search.models import Job
from .forms import SearchBarForm

from django.db.models import Q

from functools import reduce
import operator

# Create your views here.

def job_search_index(request):
    jobs = Job.objects.all()

    query = ""
    results = None

    form = SearchBarForm()
    if request.method == 'POST':
        form = SearchBarForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["query"]
            if ',' in query:
                query = query.split(',')
            else:
                query = query.split(' ')

            print(query)

            descResults = Job.objects.filter(reduce(operator.and_, [Q(description__icontains=term) for term in query]))
            cityResults = Job.objects.filter(reduce(operator.and_, [Q(city__icontains=term) for term in query]))
            stateResults = Job.objects.filter(reduce(operator.and_, [Q(state__icontains=term) for term in query]))
            results = descResults | cityResults | stateResults
    else:
        form = SearchBarForm()

    context = {
        'jobs': jobs,
        'form': form,
        'query': query if query else "",
        'results': results
    }
    return render(request, 'job_search_index.html', context)

def job_detail(request, pk):
    job = Job.objects.get(pk=pk)
    context = {
        'job': job
    }
    return render(request, 'job_detail.html', context)