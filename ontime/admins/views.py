from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import cache_control


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adminDashboard(request):
    return render(request, 'Admin/dashboard.html')
