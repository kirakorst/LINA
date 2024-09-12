from django.shortcuts import render, redirect
from .forms import SearchForm
from .models import SearchQuery

def search_view(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('search:search_results')
    else:
        form = SearchForm()
    return render(request, 'search/search.html', {'form': form})

def search_results_view(request):
    search_queries = SearchQuery.objects.all()
    context = {'search_queries': search_queries}
    return render(request, 'search/search_results.html', context)