from django.shortcuts import render
from django.http import JsonResponse
from .models import LogCategory, BuildLogEntry

def category_list(request):
    categories = Category.objects.all()
    return JsonResponse(data)

