from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

def home_page(request):
    context = {
        "inventory_list":["Widget 1","Widget 2","Widget 3"],
        "greeting" : "THAnk you FOR visiTING"
    }
    return render(request,"home.html",context)

class AboutPage(TemplateView):
    template_name = "about.html"
