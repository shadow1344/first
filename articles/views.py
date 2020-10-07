from django.shortcuts import render
from . import models
# Create your views here.

def articles_list(request):
    article =  models.Article.objects.all().order_by('date')
    arg = {'art':article}
    return render(request,'articles/articleslist.html',arg)
